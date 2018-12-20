from double_link_list import DLNode
from double_link_list import LinkedListUnderflow


class DLCList:
    """
    不在有 _head 元素，头元素舍弃，以 self._rear.next_ 指向头元素
    """

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = DLNode(elem)  # 注意关注这里p的节点创建
        if self._rear is None:
            # 建立一个节点的环
            p.next_ = p
            p.prev = p
            self._rear = p
        else:
            # 原对象的首元素 变为 首节点p 的下一个元素
            p.next_ = self._rear.next_
            p.prev = self._rear
            self._rear.next_ = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next_

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of DLCList')
        p = self._rear.next_
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next_ = p.next_
            p.next_.prev = self._rear
        return p.elem

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop_last of DLCList')
        p = self._rear.prev
        if self._rear is p:
            self._rear = None
        else:
            p.next_ = self._rear.next_
            self._rear.next_.prev = p

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
    mlist1 = DLCList()
    print(mlist1.is_empty())
    mlist1.printall()
    mlist1.prepend(999)
    mlist1.printall()

    # 链首插入元素
    for i in range(10):
        mlist1.prepend(i)

    # 尾部插入元素
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()

    mlist1.pop()
    mlist1.printall()

    mlist1.pop()
    mlist1.printall()


    mlist1.pop_last()
    mlist1.printall()

    mlist1.pop_last()
    mlist1.printall()
