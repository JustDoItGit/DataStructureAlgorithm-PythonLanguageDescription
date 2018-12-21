def reverse(lst):
    elems = lst
    i, j = 0, len(elems) - 1
    while i < j:  # 直到两个下标碰头时操作完成
        elems[i], elems[j] = elems[j], elems[i]
        i, j = i + 1, j - 1
    return elems


if __name__ == '__main__':
    print(reverse([4, 3, 2, 6]))
