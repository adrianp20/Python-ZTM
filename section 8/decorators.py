# Decorators - allow us to add extra functionality to an existing function

# decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)
# @my_decorator
def bye():
    print('see ya later')    
    
hello('hi')








# higher order function (HOC)
# def greet(func):
#     func()
# map()
# filter()
# def greet2():
#     def func():
#         return 5
#     return func


# def hello(func):
#     func()
    
# def greet():
#     print('still here!')

# a = hello(greet)
# print(a)