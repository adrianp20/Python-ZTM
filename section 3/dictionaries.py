# dictionaries

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4,5,6],
        'b': 'hello',
        'x': True 
    }
]

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}


user2 = dict(name='John')

# grabs the first item in the list, then the key 'a' and then the third item in the list 'a'
print(my_list[0]['a'][2])
print(dictionary['b'])

# if age does not exist, then it will return 55
print(user.get('age', 55))
print(user2)

print(user.update({'age': 55, 'name': 'John'}))
print(user)