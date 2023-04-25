# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(list(map(multiply_by2, [1, 2, 3])))
# # print(multiply_by2([1,2,3]))

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, [1, 2, 3])))