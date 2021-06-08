# Check whether the whole list is palindrome or not.

num = [1,2,3,4,3,2,1]
num_str = [str(x) for x in num]

num_int = ' '.join(num_str)
temp = num_int
temp = temp[::-1]
temp = temp

if temp == num_int:
	print(num,'is a palindrome')
else:
	print(num,'is not a palindrome')
