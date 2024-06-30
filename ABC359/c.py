"""python_template"""

from collections import deque


def tile_id(x, y):
    if (x + y) % 2 == 0:
        return (x // 2, y)
    else:
        return ((x - 1) // 2, y)


def bfs(start, goal):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        (x, y), cost = queue.popleft()

        if (x, y) == goal:
            return cost

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                if tile_id(x, y) == tile_id(nx, ny):
                    queue.append(((nx, ny), cost))
                else:
                    queue.append(((nx, ny), cost + 1))

    return -1  # goalが見つからない場合


def main():
    """main function"""
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    start = (sx + 0.5, sy + 0.5)
    goal = (tx + 0.5, ty + 0.5)

    start_tile = tile_id(*start)
    goal_tile = tile_id(*goal)

    result = bfs(start_tile, goal_tile)
    print(result)


if __name__ == "__main__":
    main()
