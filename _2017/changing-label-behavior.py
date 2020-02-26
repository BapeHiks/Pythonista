# https://forum.omz-software.com/topic/4183/how-to-add-a-new-line-in-a-button-title/3

import objc_util
import ui

NSLineBreakByWordWrapping = 0
NSLineBreakByCharWrapping = 1
NSLineBreakByClipping = 2
NSLineBreakByTruncatingHead = 3
NSLineBreakByTruncatingTail = 4
NSLineBreakByTruncatingMiddle = 5 # По умолчанию для меток кнопок.

b = ui.Button() # Ваша кнопка (здесь не нужно создавать, она может быть откуда-то еще, например, файл UI).
objc_util.ObjCInstance(b).button().titleLabel().setLineBreakMode(NSLineBreakByWordWrapping) # Вы можете использовать любой из перечисленных выше режимов разрыва строки.
