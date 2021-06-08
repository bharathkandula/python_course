#Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

n = int(input('Enter the iteration number:'))
sum = 0
for i in range (1,n+1):
	x = int('2' * i)
	sum += x
print(sum)