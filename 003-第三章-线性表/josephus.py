from single_cycle_link_objectList import LCList
import time


def josephus_a(n, k, m):
    """ 约瑟夫环基于数组的解O(n^2*log(n)) """
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                # print(people[i], end='')
                people[i] = 0
            i = (i + 1) % n  # 精髓
        if num < n - 1:
            # print(', ', end='')
            pass
        else:
            # print('')
            pass
    return


def josephus_l(n, k, m):
    """ 约瑟夫环基于顺序表的解O(n^2) """
    people = list(range(1, n + 1))

    num, i = n, k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        people.pop(i)
        # print(people.pop(i), end=(', ' if num > 1 else '\n'))

    return


class Josephus(LCList):
    """ 约瑟夫环基于单链表的解O(n) + O(m*n) = O((m+1)*n) """

    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next_

    def __init__(self, n, k, m):
        super().__init__()
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1)
        while not self.is_empty():
            self.turn(m - 1)
            self.pop()
            # print(self.pop(), end='\n' if self.is_empty() else ', ')


if __name__ == '__main__':
    start_a = time.time()
    josephus_a(10000, 20, 700)
    end_a = time.time()
    print('josephus_a cost: %fs' % (end_a - start_a))

    start_l = time.time()
    josephus_l(10000, 20, 700)
    end_l = time.time()
    print('josephus_l cost: %fs' % (end_l - start_l))
    start_link = time.time()
    Josephus(10000, 20, 700)
    end_link = time.time()
    print('josephus_link cost: %fs' % (end_link - start_link))
