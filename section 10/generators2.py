# iterable - something that can be iterated over
# iterate - one by one check each item in the collection
# generators - iterable, but you can only iterate over once (subset of iterables)
# difference between generators and iterable is how you implement them

def gen_fun(num):
    for i in range(num):
        yield i

for item in gen_fun(100):
    print(item)

# g = gen_fun(100)
# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     print('1')
#     for i in range(100000000):
#         i*5
        
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000000)):
#         i*5
        
# long_time()
# long_time2()










# def generator_function(num):
#     for i in range(num):
#         yield i*2 # yield keyword pauses the function and comes back to it when called again
        
        
# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))

# for item in generator_function(1000):
#     print(item)



# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(list(range(1000)))