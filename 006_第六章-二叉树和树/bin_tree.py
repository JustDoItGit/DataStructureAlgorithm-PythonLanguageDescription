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


def make_sum(a, b):
    # return ('+', a, b)
    return '+', a, b


def make_prod(a, b):
    return '*', a, b


def make_diff(a, b):
    return '-', a, b


def make_div(a, b):
    return '/', a, b


def is_basic_exp(a):
    return not isinstance(a, tuple)


def is_number(x):
    return isinstance(x, int) or isinstance(x, float) or isinstance(x, complex)


if __name__ == '__main__':
    t1 = bintree(2, bintree(4), bintree(8))
    set_left(left(t1), bintree(5))
    e1 = make_prod(3, make_sum(2, 5))
    print(e1)
    print(make_sum(make_prod('a', 2), make_prod('b', 7)))
    print(is_number(3.33))
