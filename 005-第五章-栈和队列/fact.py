def fact(n):
    """ 不支持负数 """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    print(fact(3))
