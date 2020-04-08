def user_info ():
    user = {'name': ' ', 'sername': ' ', 'born date': ' ', 'city': ' ', 'email': ' ', 'tel number': ' '}
    for f in user.keys():
        user_data = input('{}: '.format(f))
        user[f] = user_data
    print(user.values())
user_info()