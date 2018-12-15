class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        """ 表头插入元素 """
        self._head = LNode(elem, self._head)

    def pop(self):
        """ 删除表头 """
        if self._head is None:  # 无节点，引发异常
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next_
        return e

    def append(self, elem):
        """ 尾部插入元素 """
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next_ is not None:
            p = p.next_
        p.next_ = LNode(elem)

    def pop_last(self):
        """ 删除最后一个元素 """
        if self._head is None:  # 空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next_ is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next_.next_ is not None:  # 知道p.next_是最后节点
            p = p.next_
        e = p.next_.elem
        p.next_ = None
        return e

    def find(self, pred):
        """
        找到满足条件pred的某个元素
        pred函数另行定义
        """
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next_

    def printall(self):
        p = self._head
        while p:  # ===> while p i not None:
            print(p.elem, end='')
            if p.next_ is not None:
                print(', ', end='')
            p = p.next_
        print('')

    def for_each(self, proc):
        """
        遍历操作每个元素
        proc: 用于操作元素的操作函数
        """
        p = self._head
        while p:
            proc(p.elem)
            p = p.next_

    def elements(self):
        """ 生成迭代器 """
        p = self._head
        while p:
            yield p.elem
            p = p.next_


mlist1 = LList()

# 链首插入元素
for i in range(10):
    mlist1.prepend(i)

# 尾部插入元素
for i in range(11, 20):
    mlist1.append(i)
mlist1.printall()

# 遍历操作
mlist1.for_each(print)

# 迭代列表
for x in mlist1.elements():
    print(x)
