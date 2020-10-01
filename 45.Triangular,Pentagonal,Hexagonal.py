import math


def triangle(a):
    return int(a*(a+1)/2)


def triangles(n):
    return [triangle(i) for i in range(1, n+1)]


def is_pent(num):
    if ((1+math.sqrt(1+24*num))/6).is_integer():
        return True


def is_hex(num):
    if ((1+math.sqrt(1+8*num))/4).is_integer():
        return True


trs = triangles(100000)
for t in trs:
    if is_pent(t):
        if is_hex(t):
            print(f"{t} is pent and hex")