# enumerate - gives you the index of the item in the list and the item itself
for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')