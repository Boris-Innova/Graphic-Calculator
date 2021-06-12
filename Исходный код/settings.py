class Settings():
	"""Класс, представяющий настройки калькулятора."""

	def __init__(self):
		"""Инициализирует статические настройки калькулятора."""

		"""Общие параметры."""
		
		# Параметры Radiobutton
		self.radcolor = 'lightgreen'
		self.radcolor2 = 'lightblue'
		self.radheight = 2
		
		# Параметры Button
		self.height = 2
		self.font = ('Verdana', 12)
		self.bg = 'black'
		self.fg = 'white'
		
		# Параметры Text
		self.height_text = 2
		self.font = 12

		"""Параметры для обычного калькулятора."""
		
		# Параметры Button
		self.width = 10
		
		# Параметры Radiobutton
		self.radwidth = 13
		
		# Параметы Text
		self.width_text = 44

		"""Параметры для инженерного калькулятора."""
		
		# Параметры Button
		self.width_e = 5
		
		# Параметры Radiobutton
		self.radwidth_e = 15
		
		# Параметы Text
		self.width_text_e = 42
