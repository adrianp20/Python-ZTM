username = 'superuser'
password = '12345'
long_string = '''
WOW
O O
---
'''

print(long_string)
first_name = 'Adrian'
last_name = 'Posadas'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation
print('hello' + ' Adrian')

print(type(str(100)))

# escape sequence
# \t = tab
# \n = new line
weather = "\t it\'s \"kind of\" sunny\n hope you have a good day"
print(weather)

# formatted strings

name = 'Adrian'
age = 23


print('hi '+ name + '. you are ' + str(age) + ' years old')
print(f'hi {name}. you are {age} years old')
print('hi {new_name}. you are {age} years old'.format(new_name = 'bob', age = 100))

# string indexes
selfish = '01234567'
        #  01234567

# [start:stop:stepover]
print(selfish[0:8:2])

quote = 'to be or not to be'

print(quote.replace('be', 'me'))

print(quote)

# booleans
name  = 'Adrian'
is_cool = False

is_cool = True

print(bool(0))

birth_year = input('what year were you born? ')
age = 2023 - int(birth_year)

print(f'your age is: {age}')


