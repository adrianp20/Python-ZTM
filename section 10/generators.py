# generators allow us to use special keyword 'yield' instead of 'return'
range(100) # this is a generator
list(range(100)) # this is a list

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)