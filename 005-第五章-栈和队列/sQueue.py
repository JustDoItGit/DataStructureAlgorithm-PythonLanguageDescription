class QueueUnderflow(ValueError):
    pass


class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len  # 存储区长度
        self._elems = [0] * init_len  # 元素存储
        self._head = 0  # 表头元素下标
        self._num = 0  # 元素个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        """ 查看队列里最早进入的元素，不删除 """
        if self._num == 0:
            raise QueueUnderflow('empty peek')
        return self._elems[self._head]

    def dequeue(self):
        """ 出队列 """
        if self._num == 0:
            raise QueueUnderflow('empty dequeue')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        """ 元素e入队 """
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        """ 扩展队列长度 """
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0


if __name__ == '__main__':
    t_sq = SQueue()
    print(t_sq.is_empty())
    for j in range(10):
        t_sq.enqueue(j)
    print('首元素:', t_sq.peek())
    for n in range(10):
        print(t_sq.dequeue())
    # print(t_sq.dequeue())
