# Очень простой первый эксперимент по созданию GUI с использованием Pythonista
# на iPad2. 
# шуметь при прикосновении. 
# внутренностей MS Windows

from scene import *
from random import random
import sound

# Базовый класс для элементов управления
class Window (Layer):
	# Создать окно по умолчанию
	def __init__(self,p,bounds):
		Layer.__init__(self, bounds)
		
		# Добавьте себя в список родительских слоев
		if p: p.add_layer(self)
		
		self.background=Color(1,1,1)
	#                       self.image = 'Змея'
	
		# По умолчанию красная граница толщиной 1,0
		self.stroke = Color(1,0,0)
		self.stroke_weight=1
		
	# Скелетные функции должны быть переопределены
	def touch_began(self,touch): pass
	def touch_moved(self,touch): pass
	def touch_ended(self,touch): pass
	
#0-
class Button (Window):
	def touch_began(self,touch):
		new_color = Color(random(), random(), random())
		self.animate('background', new_color, 1.0)
		sound.play_effect('Crashing')
#0-

class MyApp (Scene):

	# Это выполняется до того, как нарисованы какие-либо кадры или слои
	def setup(self):
	
		# Это наш фоновый холст (весь дисплей)
		p = self.root_layer = Layer(self.bounds)
		
		center = self.bounds.center()
		
		# Создайте 2 примитивные кнопки в качестве дочерних элементов корневого слоя
		Button(p,Rect(center.x + 80, center.y + 80, 128, 128))
		Button(p,Rect(center.x - 80, center.y - 80, 128, 128))
		
	def draw(self):
		# Белый фон - в основном display.clear () перед перерисовкой
		background(1, 1, 1)
		
		self.root_layer.update(self.dt)
		self.root_layer.draw()
		
	def touch_began(self, touch):
		l=touch.layer
		if l is Window: l.touch_began(touch)
		
	def touch_moved(self, touch):
		l=touch.layer
		if l is Window: l.touch_moved(touch)
		
	def touch_ended(self, touch):
		l=touch.layer
		if l is Window: l.touch_ended(touch)
		
run(MyApp())
