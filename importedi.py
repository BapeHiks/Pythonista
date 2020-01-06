# coding: utf-8

# @tdamdouni gists
# https://gist.github.com/62fde7c2279a4fcf95385ff20073770c

# файл, необходимый для Editorial Workflow

# импортировать открытый файл в редакторе (Editorial) в Pythonista с тем же именем файла и входным

# Соответствующий Editorial рабочий процесс -> http://www.editorial-workflows.com/workflow/5898623862702080/55sNlKsa9xc

import clipboard

cbd = clipboard.get().split('\n')
prevcbd = cbd[0]
text = ''.join(clipboard.get().split('\n')[2:])
title = clipboard.get().split('\n')[1]
open(title, 'w').write(text)
clipboard.set(prevcbd)

