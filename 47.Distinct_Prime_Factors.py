import math


def is_prime(p):
    if p == 1:
        return False
    for i in range(2, math.floor(math.sqrt(p))+1):
        if p % i == 0:
            return False
    return True


def prime_factors(n):
    pfs = []
    if is_prime(n):
        pfs.append(n)
    else:
        while n % 2 == 0:
            pfs.append(2)
            n /= 2
        for p in range(3, int(n+1), 2):
            if n % p == 0 and is_prime(p):
                pfs.append(int(p))
                n = int(n / p)
    return pfs

n = 1000
consecutives = []
CONSECUTIVES = 4
i = 2
while len(consecutives) < CONSECUTIVES:
    p_factors = prime_factors(i)
    num_unique_factors = len(set(p_factors))
    if num_unique_factors == CONSECUTIVES:
        consecutives.append(i)
    else:
        consecutives = []
    i+=1
print(consecutives)