from stack import SStack


def fact(n):
    """ 不支持负数 """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def norec_fact(n):  # 自己管理栈，模拟函数调用过程
    res = 1
    st = SStack()
    while n > 0:
        st.push(n)
        n -= 1
    while not st.is_empty():
        res *= st.pop()
    return res


def norec_fact_ls(n):
    res = 1
    st = []
    while n > 0:
        st.append(n)
        n -= 1
    while st:
        res *= st.pop()
    return res


if __name__ == '__main__':
    print(fact(3))
    print(norec_fact(4))
    print(norec_fact_ls(4))
