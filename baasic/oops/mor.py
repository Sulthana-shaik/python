class A:
    pass

class B(A):
    pass

class C(A):
    pass
class D(B, C):
    pass
# creating an instance
d = D()
print(D.mro())