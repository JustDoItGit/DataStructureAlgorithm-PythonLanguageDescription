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


# 二叉树的应用
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


def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError('Unknown operator:', op)


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and a == 0:  # 没必要
        return b
    if is_number(b) and b == 0:  # 没必要
        return a
    return make_sum(a, b)


def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    # if is_number(a) and a == 0:  # 没必要
    #     return b
    # if is_number(b) and b == 0:  # 没必要
    #     return a
    return make_diff(a, b)


def eval_prod(a, b):
    # if is_number(b) and b == 0:
    #     raise ZeroDivisionError
    # if is_number(a) and a == 0:
    #     return 0
    if is_number(a) and is_number(b):
        return a * b
    return make_prod(a, b)


def eval_div(a, b):
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    # if is_number(a) and a == 0:
    #     return 0
    if is_number(a) and is_number(b):
        return a / b
    return make_div(a, b)


if __name__ == '__main__':
    t1 = bintree(2, bintree(4), bintree(8))
    set_left(left(t1), bintree(5))
    e1 = make_prod(3, make_sum(2, 5))
    print(e1)
    print(make_sum(make_prod('a', 2), make_prod('b', 7)))
    print(is_number(3.33))
    print(eval_exp(e1))
