# oop
# camelcase for class names
# class BigObject: # class
#     pass

# obj1 = BigObject() # instanciate

# print(type(obj1))

class PlayerCharacter:
    membership = True # class object attribute
    def __init__(self, name= 'anonymous', age= 0): # constructor
        if(age > 18):
            self.name = name
            self.age = age
            
    # cant use PlayerCharacter.name because it is not a class object attribute
    def shout(self):
        print(f'my name is {self.name}')
    # def run(self, hello):
    #     print(f'my name is {self.name}')
        
    @classmethod # decorator
    # cls is a convention for class
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @staticmethod # decorator
    # does not have access to class or instance (cls) 
    def adding_things(num1, num2):
        return num1 + num2
        

player1  = PlayerCharacter('Tom', 20)

print(player1.adding_things(2, 3))


        
# player1 = PlayerCharacter('Cindy', 24)
# player2 = PlayerCharacter('Tom', 21)
# player2.attack = 50



# print(player1.shout())
# print(player2.shout())
# print(player1.run('hello'))
# print(player1.name, player1.age)
# print(player2.name, player2.age)
# print(player2.attack)
# print(player1.membership)
# print(player2.membership)

# help(list)