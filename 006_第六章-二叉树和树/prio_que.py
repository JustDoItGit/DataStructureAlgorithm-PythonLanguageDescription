class PrioQueueError(ValueError):
    pass


class PrioQue:
    def __init__(self, elist=None):
        if elist is None:
            elist = []
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        """ 平均复杂度O(n) """
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        """ 平均复杂度O(1) """
        return not self._elems

    def peek(self):
        """ 平均复杂度O(1) """
        if self.is_empty():
            raise PrioQueueError('in top')
        return self._elems[-1]

    def dequeue(self):
        """ 平均复杂度O(1) """
        if self.is_empty():
            raise PrioQueueError('in top')
        return self._elems.pop()


if __name__ == '__main__':
    prioque = PrioQue([1, 2])
    for i in range(2, 9):
        prioque.enqueue(i)

    print(prioque.is_empty())
    print(prioque.peek())
    print(prioque.dequeue())
