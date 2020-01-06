#!python2

# https://gist.github.com/palmin/d31cd80309e7f01469803733d2e43c2e

# coding: utf-8
#
# Этот скрипт предназначен для использования из расширения действий Pythonista, когда Safari показывает
# a GitHub Pull Request и попросит Рабочую копию слить pull pull-запрос, таким образом, полностью заполнив его.
# Вам уже нужно клонировать этот репозиторий в рабочей копии.
#
# Он работает только в общедоступных репозиториях, поскольку в сценарии отсутствует способ авторизации, но
# происходящее в рабочей копии может быть полностью авторизовано либо с помощью ключа SSH, либо имени пользователя / пароля
#
# Вы можете прочитать о Pythonista на
# You can read about Pythonista at
#   http://omz-software.com/pythonista/
# and Working Copy at
#   https://WorkingCopyApp.com/

# Я хотел бы услышать ваши отзывы, и я @palmin в Твиттере.
#

import appex
import requests
import re
import urllib
import webbrowser
from objc_util import *

# Вам необходимо заполнить ключ значением из настроек URL Callback в рабочей копии.
key = ""

def main():
	if key == "":
		print("You need to fill out key with value from Working Copy settings.")
		quit()
		
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test data...\n')
		url = "https://github.com/owner/reponame/pull/1"
	else:
		url = appex.get_url()
		
	if url:
		# Разберите и убедитесь, что это запрос на включение
		m = re.compile('^https:\/\/github\.com/([^/]+)\/([^/]+)/pull/([0-9]+)$').match(url)
		if m == None:
			print("URL does not look like GitHub Pull Request:\n " + url)
			quit()
			
		# получить запрос на извлечение через API
		owner = m.group(1)
		repo = m.group(2)
		pr = m.group(3)
		url = "https://api.github.com/repos/%s/%s/pulls/%s" % (owner, repo, pr)
		req = requests.get(url)
		json = req.json()
		
		# выбрать то, что нам нужно
		baseRemote = json["base"]["repo"]["clone_url"]
		baseBranch = json["base"]["ref"]
		headRemote = json["head"]["repo"]["clone_url"]
		headBranch = json["head"]["ref"]
		
		# Нам нужно оформить ветку, получить последние коммиты, объединить и вернуть обратно.
		# Это может быть объединено в одну команду x-callback-url для лучшего синтаксиса.
		# Узнайте больше на
		# http://workingcopyapp.com/url-schemes.html#chain
		callback = "working-copy://x-callback-url/chain?repo=%s&key=%s" % (urllib.quote(baseRemote), urllib.quote(key))
		
		# убедитесь, что базовая ветвь проверена
		callback += "&command=checkout&branch=%s" % (urllib.quote(baseBranch))
		
		# тянуть, чтобы получить последние коммиты
		callback += "&command=pull"
		
		# слияние с головой, создание и извлечение из головы удаленного, если отсутствует
		callback += "&command=merge&branch=%s&remote=%s&create=1" % (urllib.quote(headBranch), urllib.quote(headRemote))
		
		# отодвинуть коммит коммит к завершению
		callback += "&command=push"
		print('callback: %s') % (callback)
		
		# webbrowser.open не работает с расширением действия
		app=UIApplication.sharedApplication()
		url=nsurl(callback)
		app._openURL_(url)
		
	else:
		print('No input URL found.')
		
if __name__ == '__main__':
	main()

