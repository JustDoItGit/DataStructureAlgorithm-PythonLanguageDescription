def naive_matching(t, p):
    """
        朴素匹配算法: 返回第一次匹配的开始下标
        复杂度: O(m*n)
    """
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


def matcting_kmp(t, p, pnext):
    """
        KMP串匹配，主函数。
        复杂度: O(n), 最坏复杂度2n
    """
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:  # i == m 说明找到匹配
        if i == -1 or t[j] == p[i]:  # 考虑p中下一个字符
            j, i = j + 1, i + 1
        else:  # 失败！考虑pnext决定的下一字符
            i = pnext[i]
    if i == m:  # 找打匹配返回其开始下标
        return j - i
    return -1  # 无匹配，返回特殊值


def gen_pnext_old(p):
    """ 生成针对p中个位置i的下一检查位置表，用于KMP算法 """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def gen_pnext(p):
    """
        生成针对p中个位置i的下一检查位置表，用于KMP算法
        有稍许修改的优化版本
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


if __name__ == '__main__':
    # t_ = '00000000000001000000000000000001'
    # p_ = '000001'
    # print(naive_matching(t_, p_))
    print(gen_pnext('QQQQQQQQ'))
