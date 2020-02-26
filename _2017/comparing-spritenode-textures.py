# https://forum.omz-software.com/topic/4345/how-to-compare-spritenode-textures
'''
Когда вы используете имя изображения для инициализации SpriteNode, он каждый раз создает новый объект текстуры (даже если вы используете одно и то же имя изображения дважды).

Я бы порекомендовал создать объект текстуры отдельно:
'''
from scene import *

tex = Texture('plc:Brown_Block')
sprite1 = SpriteNode(tex)
sprite2 = SpriteNode(tex)

print(sprite1.texture == sprite2.texture) # <- should be `True`
	JonB vor 14 Stunden geschrieben antworten zitieren  0
There is really no way to do it. Use another custom attribute instead, or subclass, or make a wrapper function to store the name

sprite1.type='backgound'
sprite2.type='enemy'
sprite3.type='enemy'

... or

class BackgroundSprite(SpriteNode):
	def __init__(self,texturename):
		SpriteNode.__init__(self,texturename)
		self._texturename=texturename
...
if type(sprite1)==BackgroundSprite:
	#do something else.  or check texturename... etc
or

def make_sprite(tex):
	s=SpriteNode(tex)
	s._texturename=tex
	
sprite1=make_sprite('plc:Brown_Block')
sprite2=make_sprite('plc:Brown_Block')
if sprite1._texturename==sprite2._texturename:
	#do something

