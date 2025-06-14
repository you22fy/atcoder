from collections import deque


def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    start, goal = None, None
    for i in range(h):
        flag = False
        for j in range(w):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "G":
                goal = (i, j)

            if start and goal:
                flag = True
                break
        if flag:
            break

    ans = bfs(start, goal, grid)
    print(ans)


def bfs(start, goal, grid):
    vertical_moves = [(0, -1), (0, 1)]
    horizontal_moves = [(-1, 0), (1, 0)]

    h = len(grid)
    w = len(grid[0])

    # move_dir:
    # 0 -> 直前が横移動
    # 1 -> 直前が縦移動
    # 2 -> 未移動
    visited = [[[False] * 3 for _ in range(w)] for __ in range(h)]

    sy, sx = start
    visited[sy][sx][2] = True
    queue = deque()
    queue.append((sy, sx, 2, 0))  # (y, x, move_dir, dist)

    gy, gx = goal

    while queue:
        cy, cx, move_dir, dist = queue.popleft()

        if (cy, cx) == (gy, gx):
            return dist

        if move_dir == 2:
            possible_moves = [(vertical_moves, 1), (horizontal_moves, 0)]
        elif move_dir == 0:
            possible_moves = [(vertical_moves, 1)]
        else:
            possible_moves = [(horizontal_moves, 0)]

        for moves, next_dir in possible_moves:
            for dy, dx in moves:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w:
                    if grid[ny][nx] != "#" and not visited[ny][nx][next_dir]:
                        visited[ny][nx][next_dir] = True
                        queue.append((ny, nx, next_dir, dist + 1))

    return -1  # 失敗


if __name__ == "__main__":
    main()
