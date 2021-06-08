# Create a list of n numbers
# Count even numbers and odd numbers

list = [1,2,5,3,6,7,12,56,843,12,9,3234,786]

even = [i for i in list if i % 2 == 0]
odd = [i for i in list if i % 2 != 0]

# for i in list:
# 	if i % 2 == 0:
# 		even.append(i)
# 	else:
# 		odd.append(i)

print('even numbers:',even,'count:',len(even))
print('odd numbers:',odd,'count:',len(odd))
