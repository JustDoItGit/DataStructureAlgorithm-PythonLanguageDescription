def reverse(lst):
    elems = lst
    i, j = 0, len(elems) - 1
    while i < j:
        elems[i], elems[j] = elems[j], elems[i]
        i, j = i + 1, j - 1
    return elems


print(reverse([4, 3, 2, 6]))
