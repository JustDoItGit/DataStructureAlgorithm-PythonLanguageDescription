import re


def sum_int(fname):
    re_int = r'\b(0|[1-9]\d*)\b'
    inf = open(fname)
    if inf is None:
        return 0
    int_list = map(int, re.findall(re_int, inf.read()))

    s = 0
    for n in int_list:
        s += n
    return s
