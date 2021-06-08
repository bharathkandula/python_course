# Take integer inputs from user until he/she presses q .Print the sum of all numbers. 

num,sum = 0,0
while True:
	num = input('Enter number:')
	if num == 'q':
		break
	sum += int(num)
print(sum)
