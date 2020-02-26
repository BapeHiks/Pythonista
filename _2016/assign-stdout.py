#coding: utf-8

'''Как сбросить стандартный вывод на стандартный после временного переназначения?'''

# https://forum.omz-software.com/topic/499/how-to-reset-stdout-to-the-normal-stdout-after-temporarily-reassigning-it/2

default_stdout = sys.stdout
file_handle = open('output_file', 'w')
try:
    sys.stdout = file_handle
    sys.stdout.write('foo bar')
finally:
    # Обязательно восстановите стандартный вывод, даже если возникнет исключение.
    sys.stdout = default_stdout
