#print minimum and maximum values in a list

list = [2, 6, 12, 56, 12, 3234, 7861, 5, 3, 7, 843, 9]

#for taking input
while True:
	x = input()
	if x == 'q':
		break
	list.append(int(x))
print(list)

# #using inbuilt functions
print(min(list) , max(list))

# # using sorted
sorted_list = sorted(list)
max = sorted_list[-1]
min = sorted_list[0]
print(min, max)

#traditional way
min = list[0]
max = list[0]
for i in range(len(list)):
	if max < list[i]:
		max = list[i]
	if min > list[0]:
		min = list[0]
print(min , max)
