 # Print the numbers which are palindrome inside the list

l = [351,221,3223,4567,333,27272,4928,10101]

for i in range(len(l)):
	list = l[i]

	temp = str(list)
	temp = temp[::-1]
	temp = int(temp)

	if temp == list:
		print(l[i])

print('are palindromes')