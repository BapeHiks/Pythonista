#!/usr/bin/env python3
# coding: utf-8

# Рабочий процесс: * В _Working Copy_ откройте репозиторий GitHub, который вы хотите скопировать в _Pythonista_ *, если ваши потребности более скромны, вы даже можете выбрать один файл или папку * Щелкните значок «Поделиться» в верхнем правом углу экрана «Рабочая копия» * Нажмите 

# Когда вы [возвращаетесь к Pythonista] (pythonista: //), ваши файлы должны находиться в каталоге «from Working Copy».

## Pythonista -> Рабочая копия: Рабочая копия имеет действие «Общий лист» __save to Working Copy (вам может потребоваться включить в «Общий лист», Подробнее ...)

# Рабочий процесс A - один файл: * Откройте интересующий файл в редакторе Pythonista * Нажмите значок гаечного ключа в правом верхнем углу * Нажмите кнопку "Поделиться ..." * Нажмите кнопку "Сохранить в рабочей копии" * Выберите репозиторий 

# Рабочий процесс B - папка или файл: * Нажмите «Редактировать» в браузере файлов Pythonista * Выберите интересующую папку или файл * Нажмите значок «Поделиться» в нижней части браузера файлов * Нажмите кнопку «Сохранить в рабочей копии» * 

# Примечание. При выборе нескольких папок или нескольких файлов обрабатывается только первая.

# __Теперь у нас есть сквозной рабочий процесс: GitHub -> Working Copy -> Pythonista -> Working Copy -> GitHub__

# См .: https://forum.omz-software.com/topic/2382/git-or-gist-workflow-for-pythonista/24.

# Сценарий Appex для копирования файла, папки или репозитория Git из приложения «Рабочая копия»

import appex, os, shutil

from_wc = os.path.abspath(os.path.expanduser('from Working Copy'))


def main():
    if appex.is_running_extension():
        file_paths = appex.get_file_paths()
        assert len(file_paths) == 1, 'Invalid file paths: {}'.format(file_paths)
        srce_path = file_paths[0]
        dest_path = srce_path.split('/File Provider Storage/')[-1]
        dest_path = os.path.join(from_wc, dest_path)
        file_path, file_name = os.path.split(dest_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        if os.path.isdir(srce_path):
            shutil.rmtree(dest_path, ignore_errors=True)
            print(shutil.copytree(srce_path, dest_path))
        else:
            print(shutil.copy2(srce_path, dest_path))
        print('{} was copied to {}'.format(file_name, file_path))
    else:
        print('''*В приложении «Рабочая копия» выберите репозиторий, файл или каталог
скопированы в Pythonista. 
Скрипт Pythonista. 
в Pythonista файлы должны быть в «из рабочей копии»
каталог.'''.replace('\n', ' ').replace('.  ', '.\n* '))

if __name__ == '__main__':
    main()
