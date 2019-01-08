def naive_matching(t, p):
    """ 朴素匹配算法：返回第一次匹配的开始下标 """
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:  # i == m 说明找到匹配
        if p[i] == t[j]:  # 字符相同！考虑下一对字符
            i, j = i + 1, j + 1
        else:  # 字符不同！考虑t的下一个位置
            i, j = 0, j - i + 1
    if i == m:  # 找打匹配返回其开始下标
        return j - i
    return -1  # 无匹配，返回特殊值


if __name__ == '__main__':
    t_ = '00000000000001000000000000000001'
    p_ = '000001'
    print(naive_matching(t_, p_))
