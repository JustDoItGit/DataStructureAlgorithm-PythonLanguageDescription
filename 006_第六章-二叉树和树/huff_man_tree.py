from bin_tree_TNodes import BinTNode
from stack_prio_que import PrioQueue


class HTNode(BinTNode):
    """
    时间复杂度：O(m*log(m))
    空间复杂度：O(m)
    """

    def __lt__(self, othernode):
        return self.dat < othernode.dat


class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)


def huff_man_tree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.dat + t2.dat
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()
