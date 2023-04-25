def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
        
print("Using a generator:")
for x in fib(21):
    print(x)
    
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b  
    return result

print("\nUsing a list:")
print(fib2(21))