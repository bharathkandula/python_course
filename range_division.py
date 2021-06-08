#From range n to m, print all the numbers divisible by 5 and 7 both

n = int(input('enter first number:'))
m = int(input(' enter second numver:'))

for i in range (n,m):
	if i%5==0 and i%7==0:
		print(i)