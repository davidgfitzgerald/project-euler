n = 10000
cubes = dict()
for i in range(1, n+1):
    cube = "".join(sorted((str(i**3))))
    if cube not in cubes:
        cubes[cube] = [i**3]
    else:
        cubes[cube].append(i**3)
        if len(cubes[cube]) == 5:
            print(cubes[cube])
            break

# print(cubes)
