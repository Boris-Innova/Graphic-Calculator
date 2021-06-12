from tkinter import *
from giu_functions import GIU
from settings import Settings

def start_calculater():

	window = Tk()
	window.geometry('480x405')
	window.title('Калькулятор')

	sets = Settings()
	giu = GIU(window, sets)

	buttons = giu.buttons
	buttons_e = giu.buttons_e
	buttons_e2 = giu.buttons_e2


	giu.check_button(buttons, buttons_e, buttons_e2)

	window.mainloop()

start_calculater()
