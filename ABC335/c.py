from collections import deque

def solver(N, queries):
    positions = deque([(i, 0) for i in range(1, N + 1)])

    ret = []
    for query in queries:
        if query[0] == 1:
            direction = query[1]
            new_head_pos = list(positions[0])
            if direction == 'U':
                new_head_pos[1] += 1
            elif direction == 'D':
                new_head_pos[1] -= 1
            elif direction == 'L':
                new_head_pos[0] -= 1
            elif direction == 'R':
                new_head_pos[0] += 1
            positions.appendleft(tuple(new_head_pos))
            positions.pop()
        elif query[0] == 2:
            p = query[1]
            position = positions[p - 1]
            ret.append(position)

    return ret

if __name__ == '__main__':
    n,q = map(int, input().split())
    queries = []
    for _ in range(q):
        i, q = input().split()
        if q.isnumeric():
            queries.append((int(i), int(q)))
        else:
            queries.append((int(i), q))
    ans = solver(n, queries)
    for a in ans:
        print(*a)
