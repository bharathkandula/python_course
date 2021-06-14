class Employee:

	# constructor
	# def __init__(self,name,salary):
	# 	self.name=name
	# 	self.salary=salary

	def others(self,name,salary):
		self.name = name
		self.salary = salary

	def show(self):
		print(self.name,self.salary)

# object for constructor
# bharath = Employee('bharath',40000)
# bharath.show()

puji = Employee()
puji.others('puji',55000)
puji.show()

anil = Employee()
anil.others('anil',35000)
anil.show()

suresh = Employee()
suresh.others('suresh',30000)
suresh.show()

Prasad = Employee()
prasad.others('prasad',75000)
prasad.show()
