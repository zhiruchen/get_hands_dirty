import sys
from tkinter import *


def hello(event):
    print('Press twice to exit')

def quit(event):
	print('Hello going')
	sys.exit()


widget = Button(None, text='Hello event')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()