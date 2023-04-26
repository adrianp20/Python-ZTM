# 'r' - read only
# 'w' - write only
# 'r+' - read and write


with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Hey it\'s me!')
    print(text)

