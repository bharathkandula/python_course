# Write a function to print n factorial.

n = int(input('Enter number:'))

def fact(x):
	f = 1
	while True:
		f *= x
		x-=1
		if x==1:
			break
	print('factorial of',n,'is',f)

fact(n)