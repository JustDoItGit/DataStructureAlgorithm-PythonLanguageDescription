class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class SStack:
    """
        基于顺序表技术实现的栈类
        用list对象 _elems存储栈中元素
        所有栈操作都映射到list操作
    """

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if not self._elems:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if len(self._elems) == 0:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

    def printall(self):
        while not self.is_empty():
            print(self.pop())

    def __str__(self):
        l_tmp = []
        while not self.is_empty():
            l_tmp.append(str(self.pop()))
        return ' '.join(l_tmp)


class LStack:
    """
        基于链接表技术实现的栈类，用LNode作为节点
    """

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow('in LStack.top()')
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow('in LStack.pop()')
        p = self._top
        self._top = p.next_
        return p.elem


if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    print(st1)
    # st1.printall()
    # while not st1.is_empty():
    #     print(st1.pop())
    # st1.top()
    # st1.pop()

    st2 = LStack()
    st2.push(3)
    st2.push(5)
    while not st2.is_empty():
        print(st2.pop())
    # st2.top()
    # st2.pop()
