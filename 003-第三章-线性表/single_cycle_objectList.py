from single_chain_class import LNode
from single_chain_class import LList
from single_chain_class import LinkedListUnderflow


class LCList:  # 循环单链表类
    """
    不在有 _head 元素，头元素舍弃，以 self._rear.next_ 指向头元素
    """

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 前端插入
        p = LNode(elem)
        if self._rear is None:
            p.next_ = p  # 建立一个节点的环
            self._rear = p
        else:
            p.next_ = self._rear.next_  # self._rear链尾，self._rear.next_链头
            self._rear.next_ = p

    def append(self, elem):  # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next_

    def pop(self):
        """ 前端弹出 """
        if self._rear is None:
            raise LinkedListUnderflow('in pop of CLList')
        p = self._rear.next_
        if self._rear is p:  # 只有一个元素
            self._rear = None
        else:
            self._rear.next_ = p.next_
        return p.elem

    def pop_last(self):
        """ 后端弹出 """
        if self._rear is None:
            raise LinkedListUnderflow('in pop_last of CLList')
        p = self._rear.next_
        if self._rear is p:  # 只有一个元素
            self._rear = None
        else:
            while p.next_ is not self._rear:
                # print(p.next_.elem)
                p = p.next_
            p.next_ = self._rear.next_
            self._rear = p
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next_
        while True:
            print(p.elem, end='')
            if p is self._rear:
                break
            else:
                print(', ', end='')
            p = p.next_
        print('')


if __name__ == '__main__':
    mlist1 = LCList()

    # 链首插入元素
    for i in range(10):
        mlist1.prepend(i)

    # 尾部插入元素
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()

    # mlist1.pop()
    # mlist1.printall()

    mlist1.pop_last()
    mlist1.printall()
    #
    # 遍历操作
    # mlist1.for_each(print)
    #
    # # 迭代列表
    # for x in mlist1.elements():
    #     print(x)
