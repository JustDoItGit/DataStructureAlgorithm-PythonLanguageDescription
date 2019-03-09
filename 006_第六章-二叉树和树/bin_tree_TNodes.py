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


# 通过生成器函数遍历二叉树
def preorder_elements(t_):
    s = SStack()
    while t_ is not None or not s.is_empty():
        while t_ is not None:
            s.push(t_.right)
            yield t_.dat
            t_ = t_.left
        t_ = s.pop()


# 非递归的后根序遍历算法
def postorder_nonrec(t_, proc):
    s = SStack()
    while t_ is not None or not s.is_empty():
        while t_ is not None:  # 下行循环，直到栈顶的两个树空
            s.push(t_)
            t_ = t_.left if t_.left is not None else t_.right  # 注意这个条件表达式的意义：能左就左，否则向右一步
        t_ = s.pop()  # 栈顶是访问结点
        proc(t_.dat)
        if not s.is_empty() and s.top().left == t_:
            t_ = s.top().right  # 栈不空且当前结点是栈顶的左子结点
        else:
            t_ = None  # 没有右子树或右子树遍历完毕，强迫退栈


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
    print('\n通过生成器函数遍历二叉树: ', end='')
    for i in preorder_elements(t):
        print(i, end='  ')
    print('\n非递归的后根序遍历算法: ', end='')
    postorder_nonrec(t, lambda x: print(x, end='  '))
