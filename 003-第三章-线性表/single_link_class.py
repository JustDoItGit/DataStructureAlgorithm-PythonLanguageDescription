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

    def filter(self, pred):
        """
        find的升级版
        找到满足条件pred的某个元素
        pred函数另行定义
        """
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
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

    def rev(self):
        """ 高效的链表反转，复杂度O(n)"""
        p = None
        # 后面的1，2，3是假设链表长度大于2有3个节点 a1,a2,a3
        while self._head:  # 1、True 2、True 3、True 4、None(跳出）
            q = self._head  # 1、a1 2、a2 3、a3
            self._head = q.next_  # 摘下原来的首节点1、head = a2 2、head = a3 3、head = None
            q.next_ = p  # 1、a1.next_ = None 2、a2.next_ = a1 3、a3.next_ = a2
            p = q  # 将刚摘下来的节点接入p引用的节点序列 1、p = a1 2、p = a2 3、p = a3
        self._head = p  # 反转后的节点序列已经做好，重置表头链接

    def sort1(self):
        if self._head is None:
            return

        crt = self._head.next_  # 从首节点之后开始处理
        while crt:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:  # 跳过小元素
                p = p.next_
            while p is not crt:  # 倒换大元素，完成元素插入的工作
                y = p.elem
                p.elem = x
                x = y
                p = p.next_
            crt.elem = x  # 回填退后一个元素x=y
            crt = crt.next_


if __name__ == '__main__':
    mlist1 = LList()

    # 链首插入元素
    for i in range(10):
        mlist1.prepend(i)

    # 尾部插入元素
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()

    # # 遍历操作
    # mlist1.for_each(print)

    # # 迭代列表
    # for x in mlist1.elements():
    #     print(x)

    mlist1.rev()
    mlist1.sort1()
    mlist1.printall()
