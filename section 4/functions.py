
# parameters are variables that are used in the function definition
# default parameters
def say_hello(name='Spongebob', emoji=' (insert emoji here)'):
    print(f'Hello, world! {name}{emoji}')

# arguments are the values that are passed to the function when it is called 
# positional arguments
say_hello('Adrian', ' (emoji)')
say_hello('Dan', ' (emoji)')
say_hello('Sam', ' (emoji)')

# keyword arguments
say_hello(emoji=' (emoji)', name='keyword')

say_hello()

# docstrings
def test(a):
    '''
    Info: this function prints the passed string argument
    '''
    print(a)

# this will print the docstring within the function
print(test.__doc__)


# *args **kwargs
# *args allows you to pass an arbitrary number of arguments to a function

# def super_func(*args):
#     print(*args)
#     return sum(args)

# print(super_func(1,2,3,4,5))

# **kwargs allows you to pass an arbitrary number of keyword arguments to a function
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

# rule of order: params, *args, default parameters, **kwargs
# example: def super_func(name, *args, i='hi', **kwargs):

# exercise: functions
def highest_even(li):
    even = []
    for num in li:
        if num % 2 == 0:
            even.append(num)
    return max(even)

print(highest_even([10,2,3,4,8,11]))

# walrus operator (:=) allows you to assign a value to a variable as part of a larger expression

a = 'hellooooooooo'

if ((n := len(a)) > 10):
    print(f"too long {n} elements")
    
while ((n := len(a)) >= 1):
    print(n)
    a = a[:-1]

print(a)