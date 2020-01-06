# http://omz-forums.appspot.com/pythonista/post/5903756180848640
# https://gist.github.com/weakmassive/2400bcca3ae2c0a6a43c

# Этот сценарий Pythonista приращения и сохраняет текущий файл.
# Я написал его, чтобы я мог быстро сохранить различные версии скриптов.
# Он предназначен для добавления в меню действий редактора.

import editor, os, re
text = editor.get_text()
if not text:
	sys.exit('Нет текста в редакторе.')
	
filename = os.path.split(editor.get_path())[1][:-3]

#finds номер в конце
num = re.split('[^\d]', filename)[-1]

#cчерт возьми, если число строки пуста
#if файл заканчивается числом, приравнять его
l = len(num)

if l >=1:
	num2 = int(num) + 1
	filename = filename[:-l] + str(num2) + ".py"
else:
	filename = filename + str(1) + ".py"
	
#wобряд нового файла
editor.make_new_file(filename, text)
