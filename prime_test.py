# Take a number from user and check whether it is prime or not. Use parameters to send the number to function.

num = int(input('Enter number:')) 

def prime(x):
	print(x)
	if x > 1:
		for i in range(2 , x):
			if(x % i) == 0:
				print(x,'is not a prime number')
				print(i,"times",x//i,"is",x)  
				break
		else:
			print(x,' is a prime number')
	else:
		print('x is not a prime number')

prime(num)