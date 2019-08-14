class DecoratedString(str):
	"""A string class that supports subtraction"""
	def __init__(self, value):
		self.string = value

	# def __add__(self, value):
	# 	if isinstance(value, str):
	# 		self.string += value
	# 	else:
	# 		return False

	def __sub__(self, value):
		if value in self.string:
			for i in range(len(self.string)):
				if self.string[i] == value[0] and self.string[i:i + len(value)] == value:
					return self.string[:i] + self.string[i + len(value):]
		else:
			return False

		

temp = DecoratedString("Hello World")
print(temp - "Hello")
