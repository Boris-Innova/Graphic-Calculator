from tkinter import *
from tkinter.filedialog import *
import fileinput
from tkinter import messagebox as mb
from tkinter import ttk
from math import *
import math
import det_trig as dt

class GIU():
	"""
	Класс, представляющий графический интерфейс калькулятора.
	Выполняет обработку всего, что ввел пользователь.
	Выполняет расчет выражения.
													"""
	
	def __init__(self, root, settings):
		"""Инициализация атрибутов."""
		self.window = root
		self.sets = settings
		
		# Создание меню
		self.menu = self.create_menu(self.window, self.sets)
		# Создание виджета Text для отображения выражения
		self.txt = self.create_text(self.window, self.sets)
		
		# Создание виджета Radiobutton для выбора типа калькулятора
		self.var = IntVar()
		self.radio_buttons = self.create_rad_buts(self.window, self.sets)
		
		# Кортежи для определения атрибута text кнопки			 
		self.msg_but = (('C', '()', '%', '/'), ('7', '8', '9', '*'), ('4', '5', '6', '-'), ('1', '2', '3', '+'), ('+/-', '0', '.', '='))
		self.msg_but_e = (('⇆', 'Rad', '√' ), ('sin', 'cos', 'tan'), ('ln', 'log', '1/x'), ('e^', 'x²', 'x^'), ('|x|', 'π', 'e'))
		self.msg_but_e2 = (('⇆', 'Rad', '∛' ), ('asin', 'acos', 'atan'), ('sinh', 'cosh', 'tanh'), ('asinh', 'acosh', 'atanh'), ('2ⁿ', 'x³', 'x!'))
		
		# Создание групп кнопок
		self.buttons = self.create_buttons(self.window, self.sets)
		self.buttons_e = self.create_buttons_e(self.window, self.sets)
		self.buttons_e2 = self.create_buttons_e2(self.window, self.sets)
		
		#  Операторы
		self.operators = {
		'+': lambda oper = '+' : self.operation(oper),  '-': lambda oper = '-' : self.operation(oper), 
		'*': lambda oper = '*' : self.operation(oper), '/': lambda oper = '/' : self.operation(oper),
		'%': lambda oper = '%' : self.operation(oper), '√': lambda oper = '√' : self.operation(oper),
		'∛': lambda oper = '∛' : self.operation(oper), 'x²': lambda oper = 'x²' : self.operation(oper),
		'x³': lambda oper = 'x³' : self.operation(oper), 'x^': lambda oper = 'x^' : self.operation(oper)
																											}
		# Тригонометрические операторы и два белых ворона
		self.trig_operators = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log', 'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh', '|x|', 'e^']
		
		# Числа, константы
		self.numbers = '0123456789'
		self.constants = ['π','e','M','R','m','r','G','c','Ɣ','L','k','σ','ℎ','p','q','E','λ','t','Г','N','ε','А','П']
		
		# Создание виджета Listbox
		self.cb = self.create_combobox(self.window, self.sets)

		# Флаг для перехода из радиан в градусы и обратно.
		self.flag_deg = True
		
		# Флаг для кнопки '⇆'
		self.flag_but = False
		
		# Флаг для виджета Combobox
		self.flag_box = False
		
	def operation(self, operator):
		if operator in '+-*/%':
			self.txt.insert(self.pos, operator)
		elif operator == '√':
			self.txt.insert(self.pos, '^(1/2)')
		elif operator == '∛':
			self.txt.insert(self.pos, '^(1/3)')
		elif operator == 'x²':
			self.txt.insert(self.pos, '^(2)')
		elif operator == 'x³':
			self.txt.insert(self.pos, '^(3)')
		elif operator == 'x^':
			self.txt.insert(self.pos, '^(')	
		
	def create_text(self, window, sets):
		"""Создает текстовый виджет."""
		txt = Text(window, width=sets.width_text, height=sets.height_text, font=sets.font)
		txt.grid(row=0, column=0, columnspan=4)
		return txt
		
	def create_rad_buts(self, window, sets):
		"""Создает две радиокнопки дя управления видом калькулятора."""
		self.var.set(0)
		rad_1 = Radiobutton(window, width=sets.radwidth, height=sets.radheight, bg=sets.radcolor, text ="Обычный", variable=self.var, value=0, command=self.change_calc)
		rad_2 = Radiobutton(window, width=sets.radwidth, height=sets.radheight, bg=sets.radcolor2, text="Инженерный", variable=self.var, value=1, command=self.change_calc)
		rad_1.grid(row=1, column=0, columnspan=1)
		rad_2.grid(row=1, column=1, columnspan=1)
		my_list = [rad_1, rad_2]
		return my_list
			
	def create_buttons(self, window, sets):
		"""Создает и возвращает группу кнопок."""
		buttons = []
		r = 1
		for tuple_ in self.msg_but:
			r += 1
			for msg in tuple_:
				button = Button(window, width=sets.width, height=sets.height, text=msg, font=sets.font, bg=sets.bg, fg=sets.fg)
				if button['text'] in '+-*/%()':
					button.config(fg='lightgreen')
				elif button['text'] == 'C':
					button.config(fg='orange')
				elif button['text'] == '=':
					button.config(bg='green')
				button.grid(row=r, column=tuple_.index(msg))
				buttons.append(button)	
		button = Button(window, width=sets.width, height=1, text='📏', font=sets.font, bg='grey', fg='black')
		buttons.append(button)
		button = Button(window, width=sets.width, height=1, text='const', font=sets.font, bg='grey', fg='black')
		button.grid(row=1, column=2)
		buttons.append(button)
		button = Button(window, width=sets.width, height=1, text='⌫', font=sets.font, bg='white', fg='green')
		button.grid(row=1, column=3)
		buttons.append(button)
		return buttons
		
	def create_buttons_e(self, window, sets):
		"""Создает кнопки для инженерного калькулятора."""
		buttons = []
		r = 1
		for tuple_ in self.msg_but_e:
			r += 1
			for msg in tuple_:
				button = Button(window, width=sets.width_e, height=sets.height, text=msg, font=sets.font, bg=sets.bg, fg=sets.fg)
				buttons.append(button)	
		return buttons
	
	def create_buttons_e2(self, window, sets):
		"""Создает кнопки для инженерного калькулятора."""
		buttons = []
		r = 1
		for tuple_ in self.msg_but_e2:
			r += 1
			for msg in tuple_:
				button = Button(window, width=sets.width_e, height=sets.height, text=msg, font=sets.font, bg=sets.bg, fg=sets.fg)
				buttons.append(button)	
		return buttons
	
	def create_messagebox(self, window, sets):
		"""Создание виджета messagebox"""
		message = mb.showinfo("Информация", "Выражение некоректно!")
	
	def create_menu(self, window, sets):
		"""Создает меню"""
		def open_file():
			self.txt.delete(1.0, END)
			id_file = askopenfilename()
			for string in fileinput.input(id_file):
				self.txt.insert(END, string)
			
		def save_file():
			saved_id_file = asksaveasfilename()
			letter = self.txt.get(1.0, END)
			f = open(saved_id_file, 'w')
			f.write(letter)
			f.close()
		
		def save_as_file():
			saved_id_file = asksaveasfilename()
			letter = self.txt.get(1.0, END)
			f = open(saved_id_file, 'w')
			f.write(letter)
			f.close()
		
		def close_program():
			if mb.askyesno("Exit", "Do you want save your result"):
				save_file()
				self.window.destroy()
			else:
				self.window.destroy()	
		main_menu = Menu(self.window)
		self.window.config(menu=main_menu)
		
		file_menu = Menu(main_menu)
		main_menu.add_cascade(label='File', menu=file_menu)
		file_menu.add_command(label='Open', command=open_file)
		file_menu.add_command(label='Save', command=save_file)
		file_menu.add_command(label='Save as', command=save_as_file)
		file_menu.add_command(label='Exit', command=close_program)
		
		edit_menu = Menu(main_menu)
		main_menu.add_cascade(label='Edit', menu=edit_menu)
		edit_menu.add_command(label='Copy', command=None)
		edit_menu.add_command(label='Cute', command=None)
		edit_menu.add_command(label='Paste', command=None)
	
	def create_combobox(self, window, sets):
		list_box = ttk.Combobox(self.window, values=self.constants)
		return list_box
	
	def call_combobox(self, event):
		formula = self.txt.get(1.0, END)
		i = int(self.txt.index(INSERT)[2:])
		pos = self.txt.index(INSERT)
		if formula[i-1] in self.constants or formula[i-1] in self.numbers or formula[i-1] == ')':
			self.txt.insert(pos, '*' + self.cb.get())
		else:
			self.txt.insert(pos, self.cb.get())
		self.cb.grid_forget()
	
	def change_calc(self):
		"""Меняет обычный калькулятор на инженерный и обратно"""
		if self.var.get() == 0: # конфигурация обычного калькулятора
			self.window.geometry('480x405')
			self.txt.configure(width=self.sets.width_text)
			self.txt.grid(row=0, column=0, columnspan=4)
			self.radio_buttons[0].grid(row=1, column=0, columnspan=1)
			self.radio_buttons[0].configure(width=self.sets.radwidth)
			self.radio_buttons[1].grid(row=1, column=1, columnspan=1)
			self.radio_buttons[1].configure(width=self.sets.radwidth)
			self.cb.grid_forget()
			r = 2
			c = 0
			if self.flag_but == False:
				for button in self.buttons_e:
					button.grid_forget()
			else:
				for button in self.buttons_e2:
					button.grid_forget()
			for button in self.buttons:
				if button['text'] == '⌫':
					button.configure(width=self.sets.width, height=1)
					button.grid(row=1, column=3)
				elif button['text'] == 'const':
					button.configure(width=self.sets.width, height=1)
					button.grid(row=1, column=2)
				else:
					button.configure(width=self.sets.width)
					button.grid(row=r, column=c)
				if c == 3:
					c = 0
					r += 1
				else:
					c += 1

				
		
		elif self.var.get() == 1: # конфигурация инженерного калькулятора
			self.window.geometry('465x405')
			self.txt.configure(width=self.sets.width_text_e)
			self.txt.grid(row=0, column=0, columnspan=7)
			self.radio_buttons[0].grid(row=1, column=0, columnspan=2)
			self.radio_buttons[0].configure(width=self.sets.radwidth_e)
			self.radio_buttons[1].grid(row=1, column=2, columnspan=2)
			self.radio_buttons[1].configure(width=self.sets.radwidth_e)
			self.cb.grid_forget()
			r = 2
			c = 0
			if self.flag_but == False:
				for button in self.buttons_e:
					button.configure(width=self.sets.width_e)
					button.grid(row=r, column=c)
					if c == 2:
						c = 0
						r += 1
					else:
						c += 1
			else:
				for button in self.buttons_e2:
					button.configure(width=self.sets.width_e)
					button.grid(row=r, column=c)
					if c == 2:
						c = 0
						r += 1
					else:
						c += 1
			r = 2
			c = 3
			for button in self.buttons:
				if button['text'] == '⌫':
					button.configure(width=self.sets.width_e, height=1)
					button.grid(row=1, column=6)
				elif button['text'] == 'const':
					button.configure(width=self.sets.width_e, height=1)
					button.grid(row=1, column=5)
				elif button['text'] == '📏':
					button.configure(width=self.sets.width_e, height=1)
					button.grid(row=1, column=4)
				else:
					button.configure(width=self.sets.width_e)
					button.grid(row=r, column=c)
				if c == 6:
					c = 3
					r += 1
				else:
					c += 1

	def change_text_button(self):
		"""Меняет содержимое кнопки при нажатии '⇆' """	
		r = 2
		c = 0
		if self.flag_but == False:	
			self.flag_but = True
			for button in self.buttons_e:
				button.grid_forget()
			for button in self.buttons_e2:
				button.grid(row=r, column=c)
				button.configure(width=self.sets.width_e)
				
				if c == 2:
					c = 0
					r += 1
				else:
					c += 1
		else:
			self.flag_but = False 
			for button in self.buttons_e2:
				button.grid_forget()
			for button in self.buttons_e:
				button.grid(row=r, column=c)
				button.configure(width=self.sets.width_e)
				
				if c == 2:
					c = 0
					r += 1
				else:
					c += 1

	def check_button(self, buttons, buttons_e, buttons_e2):
		"""Проверяет нажатие кнопки"""
		for button in self.buttons:
			button.bind('<Button-1>', lambda event, message=button['text'] : self.click_button(event, message))

		for button in self.buttons_e:
			button.bind('<Button-1>', lambda event, message=button['text'] : self.click_button(event, message))

		for button in self.buttons_e2:
			button.bind('<Button-1>', lambda event, message=button['text'] : self.click_button(event, message))
		
		self.cb.bind("<<ComboboxSelected>>", self.call_combobox)

	def eval_(self, formula_string):
		"""Определяет значение выражения."""
		if self.flag_deg == True:
			sin = dt.sin
			cos = dt.cos
			tan = dt.tan
			asin = dt.asin
			acos = dt.acos
			atan = dt.atan
		formula = ''
		index = -1
		for i in formula_string:
			index += 1
			if i == '^':
				formula += '**'
			elif i == 'π':
				formula += 'pi'
			elif i == 'n' and formula_string[index-1] == 'l':
				formula += 'og'
			elif i == 'g':
				formula += 'g10'
			elif i == 'M':
				formula += '(1.9891*10**30)'
			elif i == 'R':
				formula += '(6.9551*10**8)'
			elif i == 'm':
				formula += '(5.97*10**24)'				
			elif i == 'r':
				formula += '(6371*10**3)'
			elif i == 'p':
				formula += '(1.672*10**(-27))'
			elif i == 'σ':
				formula += '(5.670*10**(-8))'
			elif i == 'Ɣ':
				formula += '(9.460*10**15)'
			elif i == 'L':
				formula += '(3.827*1026)'
			elif i == 'q':
				formula += '(1.602*10**(-19))'
			elif i == 'E':
				formula += '(9.1*10**(-31))'
			elif i == 'λ':
				formula += '(2.426*10**(-12))'
			elif i == 'А':
				formula += '(149597870700)'
			elif i == 'П':
				formula += '(3.09*10**16)'
			elif i == 't' and formula_string[index+1] != 'a':
				formula += '(273)'
			elif i == 'Г':
				formula += '(365.242)'
			elif i == 'N':
				formula += '(6.022*10**23)'
			elif i == 'ε':
				formula += '149597870700'
			elif i == 'G':
				formula += '(6.674*10**(-11))'
			elif i == 'ℎ':
				formula += '(6.626*10**(-34))'																																																											
			else:
				formula += i
		# возвращаем результат
		return eval(formula)
		
	def click_button(self, event, message):
		"""Обрабатывает нажатие кнопки."""
		formula = self.txt.get(1.0, END) # получает всё, что находится в виджете Text
		next_item = message # приходящий элемент
		
		i = int(self.txt.index(INSERT)[2:])	# индекс текущего положения курсора
		pos = self.txt.index(INSERT) # индекс текущего положения курсора для метода insert
		pos_ = ''
		if int(pos[2:]) == 0 or int(pos[2:]) == 1:
			pos_ = '1.0'
		else:
			k = str(int(int(pos[2:]) - 1))
			pos_ = '1.' + k
				
		if next_item in self.numbers: # если элемент является цифрой, то
			if formula[0] == '0' and len(formula) == 2: # если первый элемент выражения 0 и он единственный, то
				self.txt.delete(pos_, pos) # 0 удаляется и
				self.txt.insert(pos, next_item) # выводится новая/другая цифра
				
			elif formula[i] in '(':
				self.txt.insert(pos, next_item + '*' )
				
			elif formula[i] in 'sctal' and pos == '1.0':
				self.txt.insert(pos, next_item + '*') # выводится * и цифра
				
			elif formula[i] in 'sctal' and formula[i-1] not in 'sincotahlgb':
				self.txt.insert(pos, '*' + next_item) # выводится * и цифра
			
			elif formula[i] in self.operators:
				self.txt.insert(pos, next_item)
				
			elif len(formula) == 1 or formula[i-1] == '.' or formula[i-1] == '(' or formula[i-1] in self.numbers or formula[i-1] in '+-*/%':
				if formula[i-1] == '0' and (formula[i-2] in self.operators or formula[i-2] == '('):
					self.txt.insert(pos, next_item)
					self.txt.delete(pos_, pos)
				else:
					self.txt.insert(pos, next_item)
			
			elif formula[i-1] == '0' and formula[i-2] not in self.numbers and formula[i-2] != '.':
				self.txt.delete(pos_, pos) # 0 удаляется и
				self.txt.insert(pos, next_item) # выводится новая/другая цифра
			
			elif formula[i-1] == ')' and formula[i] not in '+-*/%' : # если курсор стоит после закрытой скобки и после нее нет '+-*/%', то
				self.txt.insert(pos, '*' + next_item) # выводится * и цифра
				
			elif formula[i-1] == '!':
				self.txt.insert(pos, '*' + next_item)
			
			elif formula[i-1] in self.constants:
				self.txt.insert(pos, '*' + next_item)
						
		elif next_item in self.constants: # если элемент является константой, то
			if len(formula) == 1:
				self.txt.insert(pos, next_item)	
				
			elif formula[i-1] in self.numbers or formula[i-1] == ')' or formula[i-1] in self.constants:
				try:
					if formula[i+1] in self.numbers or formula[i+1] in self.constants or formula[i+1] == '(' or formula[i+1] in 'sctal':
						self.txt.insert(pos, '*' + next_item + '*')
				except:
					self.txt.insert(pos, '*' + next_item)
			
			elif formula[i-1] in '+-*/%' or formula[i-1] == '(':
				self.txt.insert(pos, next_item)
			
			elif formula[i-1] == '!':
				self.txt.insert(pos, '*' + next_item)				
			
			elif formula[i] in 'sctal' and pos == '1.0':
				self.txt.insert(pos, next_item + '*') # выводится * и цифра
				
			elif formula[i] in 'sctal' and formula[i-1] not in 'sincotahlgb':
				self.txt.insert(pos, '*' + next_item) # выводится * и цифра

		elif next_item in self.operators: # если элемент является оператором, то
			self.pos = pos
			self.pos_ = pos_
			if formula[i-1] in '1234567890)' or formula[i-1] in self.constants:
				self.operators[next_item]()
					
			elif formula[i-1] in self.operators and formula[i-2] != '(':
				self.operators[next_item]()
				self.txt.delete(pos_, pos)
				
			elif formula[i-1] == ')':
				self.operators[next_item]()
				
			elif formula[i-1] == '(' and next_item in '+-':
				self.operators[next_item]()
				
			elif formula[i-1] in '+-' and formula[i-2] == '(' and next_item in '+-':
				self.txt.delete(pos_, pos)
				self.operators[next_item]()
			
			elif formula[i-1] == '!':
				self.operators[next_item]()
			
			elif formula[i] in 'sctal' and next_item in '+-*/%' and formula[i-1] in '1234567890)':
				self.operators[next_item]()

		elif next_item in self.trig_operators: # если элемент является тригонометрическим оператором, то
			
			if len(formula) == 1 or formula[i-1] == '(':
				if next_item == '|x|':
					self.txt.insert(pos, 'abs(')
				elif next_item == 'e^':
					self.txt.insert(pos, next_item + '(')
				else:
					self.txt.insert(pos, next_item + '(')
					
			elif formula[i-1] in '1234567890' or formula[i-1] in self.constants:
				if next_item == '|x|':
					self.txt.insert(pos, '*abs(')
				elif next_item == 'e^':
					self.txt.insert(pos, '*e^(')
				else:
					self.txt.insert(pos, '*' + next_item + '(')
			
			elif formula[i-1] in self.operators:
				if next_item == '|x|':
					self.txt.insert(pos, 'abs(')
				else:
					self.txt.insert(pos, next_item + '(')
					
			elif formula[i-1] == '!':
				if next_item == '|x|':
					self.txt.insert(pos, '*abs(')
				else:
					self.txt.insert(pos, '*' + next_item)
			
			elif formula[i-1] == ')':
				if next_item == '|x|':
					self.txt.insert(pos, '*abs(')
				elif next_item == 'e^':
					self.txt.insert(pos, '*e^(')
				else:
					self.txt.insert(pos, '*' + next_item + '(')
			
			elif formula[i] in '1234567890cstla':
				if next_item == '|x|':
					self.txt.insert(pos, 'abs(')
				else:
					self.txt.insert(pos, next_item + '(')
					
		elif next_item == '()': # если элемент является скобкой, то
			if len(formula) == 1: # если строка пуста, то
				self.txt.insert(pos, '(') # выводится открывающая скобка
				
			elif formula[i-1] == '(': # если предыдущий элемент открывающая скобка, то
				self.txt.insert(pos, '(') # выводится открывающая скобка
				
			elif (formula[i-1] in '1234567890' and formula[i] in '1234567890') : # если предыдущий элемент число и следующий элемент число, то
				self.txt.insert(pos, '*(') # выводится '*('
				
			elif (formula[i-1] in '1234567890' or formula[i-1] in self.constants) and formula.count('(') > formula.count(')'): # если предыдущий элемент число и открывающих скобок больше, то
				self.txt.insert(pos, ')') # выводится закрывающая скобка
				
			elif formula[i-1] in '1234567890!' or formula[i-1] in self.constants: # если предыдущий элемент число или константа, то
				self.txt.insert(pos, '*(') # выводится '*('
				
			elif formula[i-1] == '.':
				None
				
			elif formula[i-1] in '1234567890' and len(formula)-2 == i: # если предыдущий элемент число и при этом последнее, то 
				self.txt.insert(pos, ')') # выводится закрывающая скобка
				
			elif formula[i-1] == ')' and formula.count('(') > formula.count(')'): # если предыдущий элемент закрывающая скобка и открывающих скобок больше
				self.txt.insert(pos, ')') # то выводится закрывающая скобка
				
			elif formula[i-1] == ')' and formula.count('(') == formula.count(')'):
				self.txt.insert(pos, '(') # выводится '*('
				self.txt.insert(pos, '*')
			# в любом другом случае выводим открывающую скобку			
			else:
				self.txt.insert(pos, '(')
	
		elif next_item == '⌫': # если элемент является '⌫', то
			self.txt.delete(pos_, pos)  # удаляем предыдущий элемент
			
		elif next_item == 'C': # если элемент является  'C', то
			self.txt.delete(0.0, END) # очищаем всё поле ввода/вывода и
					
		elif next_item == '+/-':	# если элемент является '+/-'
			
			if len(formula) == 1: # если поле ввода/вывода пустое, то
				self.txt.insert(END, '(-') # выводим '(-'
							
			elif formula[i-1] == '-' and formula[i-2] == '(':	# если два последних элемента это '(-', то
				pos_ = pos_[0:2] + str((int(pos_[2:]) - 1))
				self.txt.delete(pos_, pos) # удаляем '(-'
			
			elif formula[i-1] in self.operators or formula[i-1] == '(':	# если предыдущий элемент оператор, то
				self.txt.insert(pos, '(-')	# выводим '(-'
			
			elif formula[i-1] in ')':	# если предыдущий элемент ')', то
				self.txt.insert(pos, '*(-')	# выводим '(-'
			
			elif formula[i-1] in '1234567890' or formula[i-1] in self.constants:	# если предыдущий элемент число или константа, то
				for k in range(len(formula[0:i]), 0, -1):	# идем справа налево
					if formula[k-1] == '-' and formula[k-2] == '(':	# если два предыдущих элемента '(-'
						pos = pos[0:2] + str(int(k))
						pos_ = pos[0:2] + str(int(k-2))
						self.txt.delete(pos_, pos) # то удаляем из поля ввода/вывода '(-'
						break
					elif formula[k-1] not in '1234567890πe.':	# предыдущий элемент не явлется числом/константой, то
						pos = pos[0:2] + str(int(k))
						self.txt.insert(pos, '(-')	# добавляем в поле ввода/вывода '(-'
						break
					elif k == 1 and formula[k-1] in '1234567890πe':	# если последний элемент число/константа, то
						self.txt.insert(1.0, '(-')	# добавляем в поле ввода/вывода '(-'

		elif next_item == '.':	# если элемент является '.', то
			new_formula = self.txt.get(1.0, pos) # получает выражение из Text до того места, где находится курсор
			my_number = ''
			for k in range(len(new_formula[0:i]), 0, -1):	# идем справа налево
				if formula[k-1] in 'πe':
					my_number += formula[k-1]
					break
				if formula[k-1] in '1234567890.':
					my_number += formula[k-1]
				else:
					break
			if my_number.count('.') == 1:
				None
			
			elif 'π' in my_number or 'e' in my_number:
				None
			
			elif formula[i] in self.numbers or formula[i-1] in self.numbers:
				self.txt.insert(pos, next_item)
			
			elif len(my_number) == 0:
				None
			

		elif next_item == '⇆':	# если элемент является '⇆', то
			self.change_text_button()
			
		elif next_item == 'Rad':	# если элемент является 'Rad', то
			if self.flag_deg == True:
				self.flag_deg = False
				self.buttons_e[1].config(text = 'Deg')
				self.buttons_e2[1].config(text = 'Deg')
			else:
				self.flag_deg = True
				self.buttons_e[1].config(text = 'Rad')
				self.buttons_e2[1].config(text = 'Rad')
		
		elif next_item == '2ⁿ':	# если элемент является '2ⁿ', то
			if len(formula) == 1:
				self.txt.insert(pos, '2^(')
			elif formula[i-1] in '+-*/%(':
				self.txt.insert(pos, '2^(')
			elif formula[i-1] in self.numbers or formula[i-1] in self.constants or formula[i-1] in '!)':
				self.txt.insert(pos, '*2^(')
			elif formula[i] in self.numbers or formula[i] in self.constants or formula[i] in '(':
				self.txt.insert(pos, '2^(')
		
		elif next_item == 'x!':	# если элемент является 'x!', то
			if formula[i-1] in '1234567890)':
				self.txt.insert(pos, '!')
				
		elif next_item == '1/x':	# если элемент является '1/x', то
			if len(formula) == 1 or formula[i-1] == '(' or formula[i-1] in self.operators :
				self.txt.insert(pos, '1/')
			elif formula[i-1] in '1234567890)πe!':
				self.txt.insert(pos, '*1/')
				
		elif next_item == 'const':
			if self.flag_box == False:
				if self.var.get() == 0:
					self.cb.configure(width=16, height=17)
					self.cb.grid(row=2, column=2)
				else:
					self.cb.configure(width=6, height=17)
					self.cb.grid(row=2, column=5)
				self.flag_box = True
			else:
				self.flag_box = False
				self.cb.grid_forget()
				
				
		elif next_item == '=':	# если элемент является '=', то
			print(formula)
			try:
				result = round(self.eval_(formula), 6)
				if float(result) == -0.0:
					result = '0'
				self.txt.delete(1.0, END)
				self.txt.insert(END, result)
			except ZeroDivisionError:
				mb.showinfo("Информация", "Пожалуйста, не делите на ноль ʕ•ᴥ•ʔ")
			except:
				self.create_messagebox(self.window, self.sets)
	
			
				
