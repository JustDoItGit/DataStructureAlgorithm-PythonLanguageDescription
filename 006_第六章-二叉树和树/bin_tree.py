def bintree(data, left_=None, right_=None):
    return [data, left_, right_]


def is_empty_bintree(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, left_):
    btree[1] = left_


def set_right(btree, right_):
    btree[2] = right_


if __name__ == '__main__':
    t1 = bintree(2, bintree(4), bintree(8))
    set_left(left(t1), bintree(5))
