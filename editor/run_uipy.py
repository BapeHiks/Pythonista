# https://gist.github.com/Phuket2/b6a437153bd99538e0b7c852de71b38d

# https://forum.omz-software.com/topic/3386/share-pyui-viewer-class-insertion

import ui, editor

'''
				ОЧЕНЬ ВАЖНЫЙ
			Чтобы файл .pyui загружался так, как вы ожидаете, в
			UI Designer, вы должны перейти на верхний уровень (без каких-либо объектов),
			вы увидите поле с именем «Custom View Class», вам нужно ввести
			ключ, который используется для атрибута WrapInstance, который передается в
			привязки param к ui.load_view.  С примером ниже вы бы
			использовать MyClass.
			bindings = {'MyClass': WrapInstance (self), 'self': self})

			Фактическое имя не важно, но они должны совпадать.

			@JonB и @omz сделали возможной эту настройку для
			bindings param.

			Вы можете увидеть нить на
        https://forum.omz-software.com/topic/3176/use-a-pyui-file-in-another-pyui-file
'''

# map the built in theme
_themes =\
        {
                'd' : 'Dawn',
                't' : 'Tomorrow',
                'sl': 'Solarized Light',
                'sd': 'Solarized Dark',
                'cg': 'Cool Glow',
                'g' : 'Gold',
                'tn': 'Tomorrow Night',
                'o' : 'Oceanic',
                'e' : 'Editorial',
        }


def WrapInstance(obj):
	class Wrapper(obj.__class__):
		def __new__(cls):
			return obj
	return Wrapper
	
	
class PYUIViewer(ui.View):
	# это действует как обычный пользовательский ui. Посмотреть класс
	# корневой вид класса является файл pyui читать в
	def __init__(self, pyui_fn, *args, **kwargs):
		ui.load_view(pyui_fn,
		bindings={'MyClass': WrapInstance(self), 'self': self})
		
		# вызова после того, как наши kwargs изменить attrs
		super().__init__(*args, **kwargs)
		
if __name__ == '__main__':
	w, h = 600, 600
	f = (0, 0, w, h)
	
	fn = 'icurr.pyui'                       # .pyui имя файла здесь
	style = 'sheet'	theme = _themes['sd']
	
	v = PYUIViewer(fn, frame=f)
	
	editor.present_themed(v,
	theme_name=theme,
	style=style,
	animated=True)

