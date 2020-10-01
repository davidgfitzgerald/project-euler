import math


def pentagon(n):
    return n*(3*n-1)/2


def pentagons(upper_limit):
    p_nums = []
    for i in range(1, upper_limit+1):
        p_nums.append(int(pentagon(i)))
    return p_nums


def is_pent(num):
    if ((1+math.sqrt(1+24*num))/6).is_integer():
        return True


pents = pentagons(3000)
for i, k in enumerate(pents):
    for j in pents[1:i]:
        if is_pent(k - j):
            if is_pent(k + j):
                print(k - j)
