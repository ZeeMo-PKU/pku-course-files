from collections import deque


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solve_water_jug_problem(A, B, C):
    if C > max(A, B) or (C % gcd(A, B) != 0):
        return "impossible"

    queue = deque([(0, 0, [])])  # (water in jug A, water in jug B, path)
    visited = set((0, 0))

    while queue:
        current_a, current_b, path = queue.popleft()

        if current_a == C or current_b == C:
            return len(path), path

        # FILL(1)
        if (A, current_b) not in visited:
            visited.add((A, current_b))
            queue.append((A, current_b, path + ["FILL(1)"]))

        # FILL(2)
        if (current_a, B) not in visited:
            visited.add((current_a, B))
            queue.append((current_a, B, path + ["FILL(2)"]))

        # DROP(1)
        if (0, current_b) not in visited:
            visited.add((0, current_b))
            queue.append((0, current_b, path + ["DROP(1)"]))

        # DROP(2)
        if (current_a, 0) not in visited:
            visited.add((current_a, 0))
            queue.append((current_a, 0, path + ["DROP(2)"]))

        # POUR(1, 2)
        amount_poured = min(current_a, B - current_b)
        new_a = current_a - amount_poured
        new_b = current_b + amount_poured
        if (new_a, new_b) not in visited:
            visited.add((new_a, new_b))
            queue.append((new_a, new_b, path + ["POUR(1,2)"]))

        # POUR(2, 1)
        amount_poured = min(current_b, A - current_a)
        new_a = current_a + amount_poured
        new_b = current_b - amount_poured
        if (new_a, new_b) not in visited:
            visited.add((new_a, new_b))
            queue.append((new_a, new_b, path + ["POUR(2,1)"]))

    return "impossible"


# Example usage
A, B, C = map(int, input().split())
result = solve_water_jug_problem(A, B, C)

if result == "impossible":
    print("impossible")
else:
    length, path = result
    print(length)
    for step in path:
        print(step)



