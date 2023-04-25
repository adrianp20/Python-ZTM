li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# data structure is a way to store and organize data in a computer so that it can be used efficiently

# list slicing
amazon_cart = [
    'notebooks', 
    'sunglasses', 
    'toys', 
    'grapes']

# lists are mutable while strings are immutable
amazon_cart[0] = 'laptop'
# list slicing creates a new list
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart[0::])

# list methods
# basket = [1, 2, 3, 4, 5]
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# adding to the end of a list

# basket.extend([100])

# print(new_list)

# removing
# basket.pop()
# basket.pop(0)
# basket.remove(4)
# new_list = basket.pop(0)
# new_list = basket.clear()
# print(new_list)

basket.sort()
# new_basket = basket.copy()
# new_basket.sort()
basket.reverse()

# print(new_basket)
# print(basket[::-1])
# print(basket)

# print(list(range(101)))

# sentence = ' '
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jose'])
print(new_sentence)

# list unpacking
# asterisk is used to unpack a list into individual variables
a,b,c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
