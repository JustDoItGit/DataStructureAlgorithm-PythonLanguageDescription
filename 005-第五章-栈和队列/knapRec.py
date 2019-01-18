def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n - 1], wlist, n - 1):
        print('Item ' + str(n) + ':', wlist[n - 1])
        return True
    if knap_rec(weight, wlist, n - 1):
        return True
    else:
        return False


if __name__ == '__main__':
    wht = 100
    wls = [10, 10, 20, 30, 50, 60]
    n_ = 6
    knap_rec(wht, wls, n_)
