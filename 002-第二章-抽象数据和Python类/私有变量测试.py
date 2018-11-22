class MyClass:
    d = 1
    _f = 1
    __g = 1

    def __init__(self):
        self.a = 1
        self._b = 1
        self.__c = 1


my = MyClass()
print(my.a)
print(my._b)
# print(my.__c) # error
print(my.d)
print(my._f)
# print(my.__g) # AttributeError: 'MyClass' object has no attribute '__g'
