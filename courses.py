all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang', 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

name = input('Enter your name:')
email = input('Enter your mail id:')

user= {
    'user_id':101,
    'name:': name,
    'email:': email,
    'courses' : []
    }

while True :
    menu = ['All courses','My courses','Edit profile']
    print('\nMain Menu\n')
    for i in range(len(menu)):
        print(f"{i+1}.{menu[i]}")
    print('0.exit')
    choice = int(input('\nSelect an option:'))

    if choice == 0:
        print('\nThank you for visiting..!!\n')
        exit(1)

    elif choice == 1:
        curr_courses= list(set(all_courses) - set(user['courses']))
        print('\nAll Courses\n')
        for i in range(len(curr_courses)):
            print(f"{i+1}.{curr_courses[i]}")
        ch = int(input('\nselect course:'))
        user['courses'].append(curr_courses[ch-1])
        print('thanks for enrolling in',curr_courses[ch-1])
    
    elif choice == 2:
        print('\nMy Courses\n')
        c = user['courses']
        for i in range(len(c)):
            print(f"{i+1}. {c[i]}")

    elif choice == 3:
        user['name'] = input('\nEnter new name:')
        user['email'] = input('Enter new email id:')
        print('\nDetails')
        print('name :',user['name'])
        print('email id :',user['email'])