from single_chain_class import LList
from single_chain_class import LNode
from single_chain_class import LinkedListUnderflow
from random import randint


class LList1(LList):
    def __init__(self):
        super().__init__()
        self._rear = None

    def prepend(self, elem):
        """
        如果原来是空表，新加入的元素的第一个节点也是最后一个节点，所以要重写方法
        :param elem:
        :return:
        """
        '''
        self._head = LNode(elem, self._head)
        if self._rear is None:  # 是空表
            self._rear = self._head
        '''
        # 优化后的方法
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:  # 是空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next_ = LNode(elem)
            self._rear = self._rear.next_

    def pop_last(self):
        if self._head is None:  # 是空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next_ is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next_.next_:  # 直到p是倒数第二个节点
            p = p.next_
        e = p.next_.elem
        p.next_ = None
        self._rear = p
        return e


if __name__ == '__main__':
    mlist1 = LList1()
    mlist1.prepend(99)
    for i in range(11, 20):
        mlist1.append(randint(1, 20))

    for x in mlist1.filter(lambda y: y % 2 == 0):
        print(x)

    mlist1.printall()
    mlist1.pop_last()
    mlist1.printall()
