import math

class Complex():
	def __init__(self, real, img):
		self.real = real
		self.imaginary = img

	def display(self):
		if self.imaginary < 0:
			print('{}{}i'.format(self.real, self.imaginary))
		else:
			print('{}+{}i'.format(self.real, self.imaginary))
	
	def add(self,  complex_num):
		real = self.real + complex_num.real
		imaginary = self.imaginary + complex_num.imaginary
		ans = Complex(real, imaginary)
		return ans
	
	def subtract(self,  complex_num):
		real = self.real - complex_num.real
		imaginary = self.imaginary - complex_num.imaginary
		ans = Complex(real, imaginary)
		return ans

	def magintude(self):
		mag = math.sqrt(self.real*self.real + self.imaginary*self.imaginary)
		print(mag)

	def multiply(self, complex_num):
		real = self.real * complex_num.real - self.imaginary * complex_num.imaginary
		imaginary = self.real * complex_num.imaginary + self.imaginary * complex_num.real
		ans = Complex(real, imaginary)
		return ans

	def conjugate(self):
		imaginary = -1 * self.imaginary
		ans = Complex(self.real, imaginary)
		return ans


	def inverse(self):
		mag_sqr = self.real*self.real + self.imaginary*self.imaginary
		real = self.real / mag_sqr
		imaginary = -1 * self.imaginary / mag_sqr
		ans = Complex(real, imaginary)
		return ans
