import math


def dio(n):
    if (n**0.5).is_integer():
        return False
    y = 1
    while True:
        x = (1+n*(y**2))**0.5
        if x.is_integer():
            return x
        y += 1


x_vals = []
for d in range(2, 1001):
    sol = dio(d)
    if d % math.floor(1001/100) == 0:
        print(f"remaining: {(1001-d)}")
    if sol:
        print(d, sol)
        x_vals.append(sol)

print(max(x_vals))
