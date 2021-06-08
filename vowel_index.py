# Give all the index values of vowels.

str = input('Enter a string:')

v = ['a','e','i','o','u']
l = list(str)

for i in l:
	for x in v:
		if i == x:
			print(l.index(i))
