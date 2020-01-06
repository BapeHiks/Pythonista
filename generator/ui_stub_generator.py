# coding: utf-8

# @omz

# https://forum.omz-software.com/topic/2447/hackathon-challenge-set-by-ccc-started-new-thread/2

# https://gist.github.com/omz/dd8e999d4640db45bba4

# Hackathon Challange: напишите код, который использует модуль проверки Python, чтобы найти все функции и методы в модуле пользовательского интерфейса, и автоматически сгенерируйте файл ui.py, который содержит те же самые функции и модули, которые заглушены (с помощью оператора pass), так, чтобы редактор типа  Sublime или PyCharm на Windoze или реальном компьютере (например, Mac) будут выполнять автозаполнение для всех функций и методов кода Pythonista ui.  Все выигрышные записи должны: 1) предоставлять правильное завершение кода для всех методов и функций пользовательского интерфейса, 2) пройти все тесты на соответствие PyCharm PEP8 (особенно длина строки) и 3) быть размещены в репозитории GitHub к 8:00 по восточному времени в понедельник, 14 декабря 2015 г.  ,  Если есть несколько записей, которые проходят вышеупомянутые тесты, то выигрывает самое короткое количество (непустых) строк кода.
# Can you complete the challenge?!?

# Stub generator for ui module
# NOTES:
# * For classes, the base class is always assumed to be `object`. This isn't correct, but it shouldn't matter much because the
# generated stubs also contain inherited methods and data descriptors. Using the actual base classes would complicate things a
# little because the class definitions would have to appear in the correct order then.
# * It's not possible to get correct argspecs for functions and methods that are implemented in C, so they're always just
# `self, *args` (for bound methods) or `*args*` (for module-level functions) in the output.

import ui
import inspect
from numbers import Number

import console
console.clear()

from StringIO import StringIO

def write_constants(s, mod):
	members = inspect.getmembers(mod)
	s.write('# Constants:\n')
	for name, value in members:
		if isinstance(value, Number):
			s.write('%s = %s\n' % (name, value))
	s.write('\n')

def write_functions(s, mod):
	members = inspect.getmembers(mod)
	s.write('\n# Functions:\n')
	for name, value in members:
		if inspect.isfunction(value):
			s.write('def %s(*args):\n    pass\n' % (name,))
	s.write('\n')

def write_classes(s, mod):
	members = inspect.getmembers(mod)
	s.write('# Classes:\n')
	for name, value in members:
		if inspect.isclass(value):
			s.write('class %s (object):\n' % (name,))
			class_members = inspect.getmembers(value)
			s.write('    def __init__(self, *args):\n        pass\n')
			for m_name, m_value in class_members:
				if inspect.isdatadescriptor(m_value):
					s.write('        self.%s = None\n' % (m_name,))
			for m_name, m_value in class_members:
				if m_name.startswith('__'):
					continue
				elif inspect.ismethoddescriptor(m_value):
					s.write('    def %s(self, *args):\n        pass\n' % (m_name,))
				elif inspect.isbuiltin(m_value):
					s.write('    def %s(cls, *args):\n        pass\n' % (m_name,))
			s.write('\n')

def main():
	s = StringIO()
	write_constants(s, ui)
	write_functions(s, ui)
	write_classes(s, ui)
	mod_str = s.getvalue()
	print mod_str
	with open('ui_stubs.py', 'w') as f:
		f.write(mod_str)

if __name__ == '__main__':
	main()
