# https://forum.omz-software.com/topic/1918/using-workflow-app-with-pythonista/11

# coding: utf-8

import sys
import console
import clipboard
import webbrowser

console.alert('argv', sys.argv.__str__(), 'OK')
clipboard.set('here is some output!')
webbrowser.open('workflow://')

# Привет! Это Ари, один из создателей Workflow.  Удивительно, что вы все пытаетесь заставить это работать!

#Workflow должен отлично работать с Pythonista, но, как некоторые из вас упоминали, в настоящее время существует проблема, которая препятствует корректной работе действия Pythonista Workflow.  Это будет исправлено в обновлении на этой неделе!  Как только обновление вышло, вот основной процесс, который я использовал для интеграции рабочих процессов со скриптами Pythonista:

# Создайте новый рабочий процесс с каким-то содержимым, которое будет передано в скрипт Pythonista.  Например, может быть текстовое действие.  Затем добавьте Run Script и Get Clipboard.

# Сделайте соответствующий скрипт Pythonista и вставьте его имя в действие Run Script в вашем рабочем процессе.  Начните с этого как ваш скрипт на python:
#import sys
#import console
#import clipboard
#import webbrowser

#console.alert('argv', sys.argv.__str__(), 'OK')
#clipboard.set('here is some output!')
#webbrowser.open('workflow://')

# В этом примере показано, как Workflow может предоставлять входные данные для сценария Python (в этом случае сценарий Python будет отображать свои входные данные в виде предупреждения) и как сценарий Python может передавать выходные данные обратно в Workflow через буфер обмена.

# (При желании вы можете сохранить буфер обмена, создав его резервную копию при запуске рабочего процесса. В начале вашего рабочего процесса добавьте Get Cilpboard и Set Variable и присвойте переменной имя. Затем в конце рабочего процесса добавьте Get  Переменная, за которой следует Set Clipboard.)
