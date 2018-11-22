class B:
    def f(self):
        self.g()

    def g(self):
        print('B.g called.')


class C(B):
    def g(self):
        print('C.g called.')


x = B()
y = C()

x.f()
y.f()
