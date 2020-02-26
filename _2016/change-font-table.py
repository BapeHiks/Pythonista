#coding: utf-8
'''Вопрос: Есть ли простой и быстрый способ установить другой текстовый шрифт для содержимого таблицы?'''
# https://forum.omz-software.com/topic/3737/tableview-font-type
import ui
elements_txt = ui.TableView()
elements_txt.text_color = 'black'
elements_txt.font= ('Courier',10)

cell = ui.TableViewCell()
cell.text_label.text_color = 'green'
cell.accessory_type = 'detail_button'

selected_cell = ui.View()
selected_cell.border_color = 'black'
selected_cell.border_width = 2
selected_cell.corner_radius = 10
selected_cell.bg_color = 'cornflowerblue'

cell.selected_background_view = selected_cell
