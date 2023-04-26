import re 

pattern = re.compile(r"(^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$)")
string = 'Adrian'
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = 'adrian$1234'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)

# at least 8 char long
# contains any sort of letters, numbers, $%#@
# has to end with a number
