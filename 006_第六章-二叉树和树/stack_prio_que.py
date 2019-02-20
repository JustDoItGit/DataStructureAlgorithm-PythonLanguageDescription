class PrioQueueError(ValueError):
    pass


class PrioQueue:
    """  Implementing  priority queues using heaps """

    def __init__(self, elist=None):
        if elist is None:
            elist = []
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)  # add a dummy element
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2  # 完全二叉树性质6.7
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2  # 完全二叉树性质6.7
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:  # invariant: j == 2*i + 1
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1  # elems[j]不大于其兄弟结点的数据
            if e < elems[j]:  # e在三者中最小，已找到了位置
                break
            elems[i] = elems[j]  # elems[j]在三者中最小，上移
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        """ 平局复杂度O(n) """
        end = len(self._elems)
        for i in range(end - 1, -1, -1):
            self.siftdown(self._elems[i], i, end)


if __name__ == '__main__':
    s_prio_que = PrioQueue([5, 1, 8, 2, 4, 4])
    print(s_prio_que.peek())
    s_prio_que.enqueue(0)
    print(s_prio_que.dequeue())
    print('------')
    while not s_prio_que.is_empty():
        print(s_prio_que.dequeue())
