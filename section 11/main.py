# importing a module
from utilities import multiply, divide
# importing a package (folder)
# import shopping.shopping_cart
from shopping.more_shopping import shopping_cart

# print(modules_in_python.multiply(3, 5))
if __name__ == '__main__':
    print(shopping_cart.buy("apple"))
    print(divide(5,2))
    print(multiply(5,2))
    print(max([1,2,3]))

    print("please print this")