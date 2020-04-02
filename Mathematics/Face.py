class Face(object):
	def __init__(self, controlPoints):
		self._P = controlPoints #List of Control Points 

	#Quadratic Basis functions 
	def _b0(self, t):
		return (1 - t)**2
	def _b1(self, t):
		return 2*(1 - t)*t
	def _b2(self, t):
		return t**2

	def x_arr(self):
		x = []
		for i in range(3):
			x.append(self._P[i].x)
		return x
	def y_arr(self):
		y = []
		for i in range(3):
			y.append(self._P[i].y)
		return y

	def P(self, t):
		return (self._P[0] * self._b0(t)) + (self._P[1] * self._b1(t)) + (self._P[2] * self._b2(t))
