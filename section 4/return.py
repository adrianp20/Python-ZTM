def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)

total = sum(10, 20)
print(total)