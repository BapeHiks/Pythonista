# coding: utf-8
# https://gist.github.com/Mr-Coxall/43b4d6bf83f3983a28a7358aa842795a

# Автор: г-н Коксалл
# Дата создания: сентябрь 2016
# Создано для: ICS3U
# Эта программа показывает разницу между локальными и глобальными переменными

import ui

variableX = 25

def local_button_touch_up_inside(sender):
    # показывает, что происходит с локальной переменной
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_answer_label'].text = str(variableZ)
        
def global_button_touch_up_inside(sender):
    # показывает, что происходит с глобальной переменной
    
    #gглобальные переменные
    #variableX = переменнаяX 1
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_answer_label'].text = str(variableZ)

view = ui.load_view()
view.present('full_screen')
