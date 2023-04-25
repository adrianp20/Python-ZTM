# # method resolution order
# class A:
#     num = 10
    
# class B(A):
#     pass

# class C(A):
#     num = 1
    
# class D(B, C):
#     pass

# # this will display the method resolution order of the class
# print(D.mro())

# #   A
# #  / \
# # B   C
# #  \ /
# #  D

class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)