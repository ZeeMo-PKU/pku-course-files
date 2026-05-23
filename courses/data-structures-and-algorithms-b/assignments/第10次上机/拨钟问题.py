from collections import deque


def move(index, state):
    new_state = list(state)
    if index == 1:
        for i in [0, 1, 3, 4]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 2:
        for i in [0, 1, 2]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 3:
        for i in [1, 2, 4, 5]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 4:
        for i in [0, 3, 6]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 5:
        for i in [1, 3, 4, 5, 7]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 6:
        for i in [2, 5, 8]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 7:
        for i in [3, 4, 6, 7]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 8:
        for i in [6, 7, 8]:
            new_state[i] = (new_state[i] + 1) % 4
    elif index == 9:
        for i in [4, 5, 7, 8]:
            new_state[i] = (new_state[i] + 1) % 4
    return tuple(new_state)


def panduan(state):
    return state == (0, 0, 0, 0, 0, 0, 0, 0, 0)


def main(initial_state):
    target_state = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    queue = deque([(initial_state, [], 1)])  # (state, path, next_move_index)
    seen = set([initial_state])

    while queue:
        current_state, path, next_move_index = queue.popleft()

        if panduan(current_state):
            return path

        for index in range(next_move_index, 10):
            new_state = move(index, current_state)
            new_path = path + [index]
            if new_state not in seen:
                seen.add(new_state)
                queue.append((new_state, new_path, index))

    return None


# Example usage
initial_state = []
for _ in range(3):
    initial_state.extend(map(int, input().split()))
initial_state = tuple(initial_state)

ans = main(initial_state)

if ans:
    print(' '.join(map(str, ans)))
else:
    print("impossible")



