class ControlPoint(object):
	def __init__(self, x_val, y_val):
		self.x = float(x_val)
		self.y = float(y_val)

	def coordinates(self):
		return [self.x, self.y]
	
	def __mul__(self, integer):
		return ControlPoint (self.x * integer, self.y * integer)

	def __add__(self, point):
		return ControlPoint (self.x + point.x, self.y + point.y)
