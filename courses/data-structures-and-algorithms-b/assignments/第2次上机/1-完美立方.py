def find_perfect_cubes(N):
    cubes = [i ** 3 for i in range(N + 1)]
    cube_set = {v: i for i, v in enumerate(cubes)}

    for a in range(2, N + 1):
        for b in range(2, a):
            for c in range(b, a):
                target = cubes[a] - cubes[b] - cubes[c]
                if target > 0 and target in cube_set and cube_set[target] >= c:
                    d = cube_set[target]
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')


if __name__ == '__main__':
    N = int(input().strip())

    find_perfect_cubes(N)