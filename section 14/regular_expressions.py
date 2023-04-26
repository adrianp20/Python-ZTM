import re

pattern = re.compile('search inside of this text please!')
string = 'search inside of this text please! Adrian'

# a = re.search('this', string)
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())
# print(b)
# print(c)
print(d)
