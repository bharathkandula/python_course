# Print following a pattern without using any loop.
# Examples : 
# Input: n = 16
# Output: 16, 11, 6, 1, -4, 1, 6, 11, 16
# Input: n = 10
# Output: 10, 5, 0, 5, 10

x = int(input('Enter number:'))
def rec(num):
	print (num)
	if num <= 0:
		return
	rec(num-5)
	print(num)
rec(x)
