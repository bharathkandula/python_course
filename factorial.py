# Write a loop to find the factorial of any number

num = int(input('enter the number:'))
sum = 1
while True:
	sum *= num
	num -= 1
	if num == 1:
		break
print(sum)