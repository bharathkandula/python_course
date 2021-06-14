sh=input('From square, rectangle and triangle\nchoose shape:')

class Shape():

	def __init__(self,shape):
		if shape == 'square':
			self.no_sides = 1
		elif shape == 'rectangle':
			self.no_sides = 2
		elif shape == 'triangle':
			self.no_sides = 3

	def input(self):
		self.side = []
		print(f'Enter {self.no_sides} sides:')
		for i in range(self.no_sides):
			self.side.append(int(input()))

class Square(Shape):
	
	def __init__(self):
		super().__init__('square')
		super().input()

	def area(self):
		print(f'area of square is {self.side[0]**2}')

class Rectangle(Shape):

	def __init__(self):
		super().__init__('rectangle')
		super().input()

	def area(self):
		print(f'area of rectangle is {self.side[0]*self.side[1]}')

class Triangle(Shape):

	def __init__(self):
		super().__init__('triangle')
		super(). input()

	def area(self):
		a,b,c = self.side
		s = (a+b+c)/2
		a = ((s-a)*(s-b)*(s-c))**0.5
		print(f'area of triangle is {a}')


s = Shape(sh)
s.__init__(sh)

if sh == 'triangle':
	t = Triangle()
	t.area()

elif sh == 'square':
	s = Square()
	s.area()

elif sh == 'rectangle':
	r = Rectangle()
	r.area()

else:
	print('entered input is invalid')
