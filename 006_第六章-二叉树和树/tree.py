import copy


class SubtreeIndexError(ValueError):
    pass


# extend在这里失效了，有待研究

def tree(data, *subtrees):
    l = [data]
    l.extend(subtrees)
    return l


def is_empty(tree_):
    return tree_ is None


def root(tree_):
    return tree_[0]


def subtree(tree_, i):
    if i < 1 or i > len(tree_):
        raise SubtreeIndexError
    return tree_[i + 1]


def set_root(tree_, data):
    tree_[0] = data


def set_subtree(tree_, i, subtree_):
    if i < 1 or i > len(tree_):
        raise SubtreeIndexError
    tree_[i + 1] = subtree_


if __name__ == '__main__':
    tree1 = tree('+', 1, 2, 3)
    tree2 = tree('*', tree1, 6, 8)
    # set_subtree(tree1, 2, tree('+', 3, 5))
