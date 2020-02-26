#coding: utf:8
# https://forum.omz-software.com/topic/3777/moving-from-one-pyui-file-to-another

import ui

main_view = ui.load_view("main.pyui")
other_view = ui.load_view("other.pyui")

# Действие кнопки в main_view, которая должна показывать второй вид
def my_button_action(sender):
	other_view.present("sheet")
	
main_view.present()

