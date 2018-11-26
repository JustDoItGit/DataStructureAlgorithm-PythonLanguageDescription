class C1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        print(self.x, self.y)


class C2(C1):
    def m1(self):
        super().m1()
        # super(C2, self).m1() # 这里是指C2的父类 python2里这么写
        print('Some special service.')


C2(1, 2).m1()
