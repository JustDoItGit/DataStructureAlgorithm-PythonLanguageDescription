def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1  # invariant: j == 2*i + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1  # elems[j]不大于其兄弟结点的数据
            if e < elems[j]:  # e在三者中最小，已找到了位置
                break
            elems[i] = elems[j]  # elems[j]在三者中最小，上移
            i, j = j, 2 * j + 1
        elems[i] = e

    end = len(elems)
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range(end - 1, 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)


if __name__ == '__main__':
    l = [3, 1, 5, 3, 4]
    heap_sort(l)
    print(l)
