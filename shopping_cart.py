List = ['chocolate','biscuit','cola','water','noodles','flour','icecream','sugar']

user = {
	'user_id' : 101,
	'cart' : []
	}

while True:
	print('\nMain Menu\n')
	menu = ['list of items','your cart']
	for i in range(len(menu)):
		print(f"{i+1}.{menu[i]}")
	print('0.exit')
	choice = int(input('\nselect an option:'))

	if choice == 0:
		print('Thank you')
		exit()

	elif choice == 1:
		items = list(set(List) - set(user['cart']))
		for i in range(len(items)):
			print(f'{i+1}.{items[i]}')
		ch = int(input('\nSelect an option:'))
		user['cart'].append(List[ch-1])
		print(f'Thanks for adding {items[ch]} into your cart')

	elif choice == 2:
		print ('\nYour Cart')
		x = user['cart']
		for i in range(len(x)):
			print(f'{i+1}.{x[i]}')
