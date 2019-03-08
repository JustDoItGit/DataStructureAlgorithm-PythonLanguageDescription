from sQueue import *
import sys

sys.path.append('../005-第五章-栈和队列')
try:
    from stack import SStack
except Exception as e:
    raise e


class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.dat = dat
        self.left = left
        self.right = right


# 统计树中结点个数
def count_bin_tnodes(t_):
    if t_ is None:
        return 0
    else:
        return 1 + count_bin_tnodes(t_.left) + count_bin_tnodes(t_.right)


# 假设结点中保存数值，求这种二叉树里的所有数值和
def sum_bin_tnodes(t_):
    if t_ is None:
        return 0
    else:
        return t_.dat + sum_bin_tnodes(t_.left) + sum_bin_tnodes(t_.right)


# 先根顺序遍历二叉树
def preorder(t_, proc):  # proc是具体的结点数据操作
    if t_ is None:
        return
    proc(t_.dat)
    preorder(t_.left, proc)
    preorder(t_.right, proc)


# 打印二叉树
def print_bin_tnodes(t_):
    if t_ is None:
        print('^', end='')  # 空树输出^
        return
    print('(' + str(t_.dat), end='')
    print_bin_tnodes(t_.left)
    print_bin_tnodes(t_.right)
    print(')', end='')


# 宽度优先遍历
def levelorder(t_, proc):
    qu = SQueue()
    qu.enqueue(t_)
    while not qu.is_empty():
        n = qu.dequeue()
        if n is None:  # 弹出的树为空则直接跳过
            continue
        qu.enqueue(n.left)
        qu.enqueue(n.right)
        proc(n.dat)


# 非递归的先根序遍历二叉树
def preorder_nonrec(t_, proc):
    """
    时间复杂性: O(n)
    空间复杂性: O(log(n))
    """
    s = SStack()
    while t_ is not None or not s.is_empty():
        while t_ is not None:
            proc(t_.dat)
            s.push(t_.right)
            t_ = t_.left
        t_ = s.pop()


if __name__ == '__main__':
    t = BinTNode(1, BinTNode(2), BinTNode(3))
    preorder(t, lambda x: print(x, end='  '))
    print()
    print(count_bin_tnodes(t))
    print(sum_bin_tnodes(t))
    t = BinTNode(1, BinTNode(2, BinTNode(5)), BinTNode(3))
    print_bin_tnodes(t)
    print('\n深度优先遍历，递归: ', end='')
    preorder(t, lambda x: print(x, end='  '))
    print('\n广度/宽度优先遍历: ', end='')
    levelorder(t, lambda x: print(x, end='  '))
    print('\n非递归的先根序遍历二叉树: ', end='')
    preorder_nonrec(t, lambda x: print(x, end='  '))
