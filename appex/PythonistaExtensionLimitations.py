# coding: utf-8

# https://forum.omz-software.com/topic/1988/launching-pythonista-from-1-6b-app-extension

# Я пытаюсь написать скрипт для расширения приложения 1.6, который будет:

 # Возьмите какой-то текст, переданный с листа
 # Форматировать текст определенным образом
 # Поместите отформатированный текст на монтажную панель
 # Запустите Pythonista и запустите другой скрипт, который возьмет текст на монтажном столе и что-то с ним сделает.

 # Можно ли запустить Pythonista:// URL из расширения приложения?  Если нет, то можно ли что-то сделать с помощью objc_util?

 # В худшем случае, я могу сделать это двухэтапным процессом, но было бы здорово иметь его в одном месте.
import appex
import clipboard
import webbrowser 

initial_text = appex.get_text()

# text processing stuff

clipboard.set(processed_text)
webbrowser.open('pythonista://NewFromClipboard.py')

# @omz
# As far as I'm aware, this is unfortunately impossible. The API that is supposed to open URLs from app extensions is [explicitly documented](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSExtensionContext_Class/#//apple_ref/occ/instm/NSExtensionContext/openURL:completionHandler:) as only being available for Today widgets, the regular one (via UIApplication) doesn't do anything either in an extension.

# In earlier versions of iOS 8, there was a workaround for this (essentially abusing a web view), but this has apparently been patched in 8.4.
