# coding: utf-8

# https://github.com/jsbain/objc_hacks/blob/master/apphack.py

''' Набор инструментов для добавления или удаления пользовательских кнопок на панели инструментов. Это может быть не очень надежно, но, кажется, работает нормально. Объекты кнопок и действия сохраняются, поэтому они сохраняются после глобальной очистки, но они не были тщательно протестированы. Если функция полагается на импорт, который произошел за пределами функции, они могут исчезнуть - пользователь должен убедиться, что эти модули добавлены в модуль, который хранится в pythonista, например что-либо в пакетах сайта, или имя начинается с __   '''

from objc_util import *
import ui,console
import weakref
from functools import partial


w=ObjCClass('UIApplication').sharedApplication().keyWindow()
main_view=w.rootViewController().view()

def get_toolbar(view):
	#get main editor toolbar, by recursively walking the view
	sv=view.subviews()
	
	for v in sv:
		if v._get_objc_classname()=='OMTabViewToolbar':
			return v
		tb= get_toolbar(v)
		if tb:
			return tb
def create_toolbar_button(action,image,index=0,tag=''):
	'''Создайте кнопку на главной панели инструментов с действием, именем изображения, местоположением индекса и строковым тэгом. кнопка и действие хранятся в __persistent_views[index].  тег позволяет найти вид с помощью tb.viewFromTag_(hash(tag)) (old idea)'''
	assert(callable(action))
	
	tb=get_toolbar(main_view)
	global __persistent_views
	try:
		__persistent_views
	except NameError:
		__persistent_views={}
	#проверить наличие кнопки в этом индексе и удалить при необходимости
	remove_toolbar_button(index)
	
	#добавить новую кнопку слева от правой кнопки. Индекс 0 находится рядом с левыми кнопками, индекс 1 дальше слева и т. д.
	#хранить, чтобы он не очищался.
	
	btn=ui.Button( frame=(tb.size().width -
	tb.rightItemsWidth()-(index+1)*40,22,40,40))
	btn.flex='L'
	btn.image=ui.Image.named(image)
	btn.action=action
	btn_obj=ObjCInstance(btn)
	btn_obj.tag=hash(tag)
	__persistent_views[index]=(btn,action,tag)
	tb.addSubview_(btn_obj)
	return btn
def remove_toolbar_button(index):
	global __persistent_views
	try:
		btn,action,tag=__persistent_views.pop(index)
		btn.action= None
		ObjCInstance(btn).removeFromSuperview()
	except KeyError:
		pass
		
if __name__=='__main__':
	def run_script(sender):
		'''запустить скрипт без очистки glbals'''
		import editor
		editor.reload_files()
		execfile(editor.get_path(),globals())
		
	create_toolbar_button(run_script,'iow:play_32',0,'execfile')

