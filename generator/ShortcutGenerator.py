# Этот скрипт добавляет ярлык "Webclip" на домашний экран.
# Ярлык может быть использован для открытия веб-страницы в полноэкранном режиме,
# или для запуска пользовательского URL (например, стороннего приложения).
# Вам будет предложено указать заголовок, URL-адрес и значок (из вашей камеры)

import plistlib
import http.server
import webbrowser
import uuid
from io import BytesIO
import Image
import photos
import notification
import console

class ConfigProfileHandler (http.server.BaseHTTPRequestHandler):
	config = None
	def do_GET(s):
		s.send_response(200)
		s.send_header('Content-Type', 'application/x-apple-aspen-config')
		s.end_headers()
		plist_string = plistlib.writePlistToString(ConfigProfileHandler.config)
		s.wfile.write(plist_string)
	def log_message(self, format, *args):
		pass

def run_server(config):
	ConfigProfileHandler.config = config
	server_address = ('', 0)
	httpd = http.server.HTTPServer(server_address, ConfigProfileHandler)
	sa = httpd.socket.getsockname()
	webbrowser.open('safari-http://localhost:' + str(sa[1]))
	httpd.handle_request()
	notification.schedule('Нажмите «Установить», чтобы добавить ярлык на рабочий стол.', 1.0)

def main():
	console.alert('Shortcut Generator', 'Этот скрипт добавляет ярлык «Webclip» на домашний экран.  Ярлык можно использовать для открытия веб-страницы в полноэкранном режиме или для запуска пользовательского URL-адреса (например, стороннего приложения). Введите название, URL-адрес и значок (из вашего альбома).', 'Continue')
	label = console.input_alert('Shortcut Title', 'Пожалуйста, введите короткое название для иконки на главном экране.', '', 'Continue')
	if not label:
		return
	url = console.input_alert('Shortcut URL', 'Пожалуйста, введите полный URL, который должен запустить ярлык.', '', 'Continue')
	if not url:
		return
	icon = photos.pick_image()
	if not icon:
		return
	console.show_activity('Подготовка профиля конфигурации...')
	data_buffer = BytesIO()
	icon.save(data_buffer, 'PNG')
	icon_data = data_buffer.getvalue()
	unique_id = uuid.uuid4().urn[9:].upper()
	config = {'PayloadContent': [{'FullScreen': True,
            'Icon': plistlib.Data(icon_data), 'IsRemovable': True,
            'Label': label, 'PayloadDescription': 'Configures Web Clip', 
            'PayloadDisplayName': label,
            'PayloadIdentifier': 'com.omz-software.shortcut.' + unique_id, 
            'PayloadOrganization': 'omz:software', 
            'PayloadType': 'com.apple.webClip.managed',
            'PayloadUUID': unique_id, 'PayloadVersion': 1,
            'Precomposed': True, 'URL': url}], 
            'PayloadDescription': label,
            'PayloadDisplayName': label + ' (Shortcut)', 
            'PayloadIdentifier': 'com.omz-software.shortcut.' + unique_id,
            'PayloadOrganization': 'omz:software', 
            'PayloadRemovalDisallowed': False, 'PayloadType': 
            'Configuration', 'PayloadUUID': unique_id, 'PayloadVersion': 1}
	console.hide_activity()
	run_server(config)

if __name__ ==  '__main__':
	main()


