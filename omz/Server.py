#coding: utf-8
'''Простой HTTP-сервер, который позволяет просматривать файлы в Pythonista из веб-браузера в локальной сети (или на этом устройстве). HTML-страницы обрабатываются с использованием шаблонизатора jinja2.'''

from SimpleHTTPServer import SimpleHTTPRequestHandler
import urlparse
import urllib
import cgi
from socket import gethostname, gethostbyname
import os
import shutil
from cStringIO import StringIO
import jinja2

PORT = 8080
with open('TemplateServer.html') as f:
	TEMPLATE = jinja2.Template(f.read())

class MyRequestHandler(SimpleHTTPRequestHandler):
	def list_directory(self, path, msg=None):
		files = os.listdir(path)
		files.sort(key=lambda a: a.lower())
		displaypath = cgi.escape(urllib.unquote(self.path))
		entries = []
		for name in files:
			if name.startswith('.'):
				continue
			fullname = os.path.join(path, name)
			displayname = linkname = name
			if os.path.isdir(fullname):
				displayname = linkname = name + '/'
			entries.append({'href': urllib.quote(linkname), 'name': cgi.escape(displayname)})
		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.end_headers()
		html = TEMPLATE.render(title=displaypath, files=entries, message=msg)
		return StringIO(html)
		
	def get_unused_filename(self, filename):
		if not os.path.exists(filename):
			return filename
		basename, ext = os.path.splitext(filename)
		suffix_n = 1
		while True:
			alt_name = basename + '-' + str(suffix_n) + ext
			if not os.path.exists(alt_name):
				return alt_name
			suffix_n += 1

	def do_POST(self):
		form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type']})
		filename = form['file'].filename
		dest_filename = self.get_unused_filename(filename)
		with open(dest_filename, 'w') as f:
			shutil.copyfileobj(form['file'].file, f)
		msg = 'Added: %s' % (dest_filename,)
		self.wfile.write(self.list_directory(os.getcwd(), msg).read())

if __name__ == '__main__':
	os.chdir(os.path.expanduser('~/Documents'))
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('', PORT), MyRequestHandler)
	print 'URL локального HTTP-сервера:'
	print 'http://%s.local:%i' % (gethostname(), PORT)
	print 'Нажмите кнопку остановки в редакторе или консоли, чтобы остановить сервер.'
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.shutdown()
		print 'Сервер остановлен'
