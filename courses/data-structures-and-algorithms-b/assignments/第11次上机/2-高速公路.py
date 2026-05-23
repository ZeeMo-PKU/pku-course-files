import sys
import math


# Disjoint Set Union (Union-Find)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # Towns are 1-indexed

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def main():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    N = int(data[idx])
    idx += 1

    coords = []
    for _ in range(N):
        x = int(data[idx])
        y = int(data[idx + 1])
        coords.append((x, y))
        idx += 2

    M = int(data[idx])
    idx += 1

    dsu = DSU(N)

    # Process existing highways
    for _ in range(M):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        dsu.union(u, v)

    # Generate all possible edges
    edges = []
    for i in range(N):
        for j in range(i + 1):
            if i == j:
                continue
            dist = distance(coords[i], coords[j])
            edges.append((dist, j + 1, i + 1))  # (distance, town1, town2)

    # Sort edges by distance
    edges.sort()

    result = []

    # Kruskal's algorithm
    for d, u, v in edges:
        if dsu.union(u, v):
            result.append((u, v))

    # Output the result
    for u, v in result:
        print(f"{u} {v}")


if __name__ == "__main__":
    main()