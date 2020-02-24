
class Matrix(object):
	"""Matrix class, implementing nxn square matrices """
	def __init__(self, n = 3, lst = None):
		"""Takes n as the order of the matrix, creates nxn Identity matrix"""
		self._n = n

		if not isinstance(lst, list):
			self.mat = [[0 for i in range(self._n)] for j in range(self._n)]
			for i in range(self._n):
				self.mat[i][i] = 1
		else:
			self.mat = lst
	
	def show(self):
		for i in self.mat:
			for j in range(self._n):
				if j == 0:
					print("[", i[j], end=" ") 
				elif j + 1 == self._n:
					print(i[j], "]")
				else:
					print(i[j], end=" ")
		print()			

	def __mul__(self, s):
		cop = [i.copy() for i in self.mat]

		for i in cop:
			for j in range(self._n):
				i[j] *= s

		return Matrix(self._n, cop)

	def __add__(self, matB):
		if not isinstance(matB, Matrix) or matB.dimensions() != self._n:
			return False

		cop = [i.copy() for i in self.mat]
		for i in range(self._n):
			for j in range(self._n):
				cop[i][j] += matB.mat[i][j]

		return Matrix(self._n, cop)

	def dimensions(self):
		return self._n

	def make_zero(self):
		self.mat = [[0 for i in range(self._n)] for j in range(self._n)]

	def matrix_multiplication(self, mat):
		assert mat.dimensions == self.n
		if mat.dimensions() != self.n:
			return False


	def __str__(self):
		"""Returns empty string"""
		self.show()
		return " "


def mat_mul(matA, matB):
	return True