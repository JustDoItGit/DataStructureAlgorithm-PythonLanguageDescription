def josephus_a(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end='')
                people[i] = 0
            i = (i + 1) % n  # 精髓
        if num < n - 1:
            print(', ', end='')
        else:
            print('')
    return


if __name__ == '__main__':
    josephus_a(10, 2, 7)
