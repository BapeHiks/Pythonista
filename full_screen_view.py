# https://github.com/cclauss/Ten-lines-or-less/blob/master/full_screen_view.py

# https://forum.omz-software.com/topic/4284/how-do-i-make-a-full-screen-button-and-handle-button-down-and-button-up-events

#сделать полноэкранную кнопку и обрабатывать события, связанные с кнопкой вниз и кнопкой?

# нажмите и удерживайте менее одной секунды, чтобы добавить «.» 
# нажмите и удерживайте одну или несколько секунд, чтобы добавить «-» к заголовку

from datetime import datetime as dt
import ui


class FullScreenButtonView(ui.View):
    def __init__(self):
        self.name = ''

    def touch_began(self, touch):
        self.tap_time = dt.now()

    def touch_ended(self, touch):
        self.name += '.' if (dt.now() - self.tap_time).total_seconds() < 1 else '-'


FullScreenButtonView().present()
