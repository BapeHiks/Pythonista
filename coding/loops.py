# https://forum.omz-software.com/topic/3258/loops

mylist = ["hello", "there", "how", "are", "you"]

for message in mylist:
	print(message)
# --------------------

import random

response = ""
while response != "exit":
	print("Ваше случайное число:", random.randint(0, 10))
	response = input()
# --------------------


