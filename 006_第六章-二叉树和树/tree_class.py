class TreeNode:
    def __init__(self, data, subs=[]):
        self._data = data
        self._subtrees = list(subs)

    def __str__(self):
        return '[TreeNode {0} {1}]'.format(self._data, self._subtrees)


class Tree:
    def __init__(self):
        self._root = None
