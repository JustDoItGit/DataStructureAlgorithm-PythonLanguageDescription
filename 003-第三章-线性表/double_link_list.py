from single_link_class import LNode
from single_link_class import LinkedListUnderflow
# from single_link_class import LList
from single_link_derived_class_tail_node_reference_field import LList1
from random import randint


class DLNode(LNode):  # 双向链表节点类
    def __init__(self, elem, prev=None, next_=None):
        super().__init__(elem, next_)
        self.prev = prev


class DLList(LList1):
    """
    head: _head头元素的prev为None
    end: _rear元素的next_为None
    NULL: 空表的head,end……所有属性都为None
    """

    def __init__(self):
        super().__init__()

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)  # 注意关注这里p的节点创建
        if self._head is None:  # 空表
            self._rear = p
        else:  # 非空列，设置prev引用
            p.next_.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)  # 注意关注这里p的节点创建
        if self._head is None:  # 空表
            self._head = p
        else:  # 非空列，设置next_引用
            p.prev.next_ = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop of DLList')
        e = self._head.elem
        self._head = self._head.next_
        if self._head:  # _head空时不需要做任何事
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last of DLList')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:  # 只有一个元素的情况，因为被删除空了
            self._head = None  # 设置_head保证is_empty正确工作
        else:
            self._rear.next_ = None
        return e


if __name__ == '__main__':
    mlist1 = DLList()
    mlist1.prepend(99)
    for i in range(11, 20):
        mlist1.append(randint(1, 20))

    for x in mlist1.filter(lambda y: y % 2 == 0):
        print(x)

    mlist1.printall()
    mlist1.pop()
    mlist1.printall()
    mlist1.pop_last()
    mlist1.printall()
