username = input('Please Input Name')
password = input('Please Input Password')

print('Your Account has been created successfully')
print('Login Now!')

username2 = input('Please Input Name')
password2 = input('Please Input Password')

if username==username2 and password==password2:
    print('Login in Successfully')
else:
    print('Invalid credentials')