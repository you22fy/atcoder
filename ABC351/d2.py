def main():
    """main function"""
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    can_start_memo = [[False] * w for _ in range(h)]  # メモ化用の2次元リスト

    grid_memo = [[None for _ in range(w)] for _ in range(h)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def can_start(x, y):
        """can_start"""
        if can_start_memo[x][y]:
            return can_start_memo[x][y]

        if grid[x][y] == "#":
            can_start_memo[x][y] = False
            return False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == "#":
                can_start_memo[x][y] = False
                return False

        can_start_memo[x][y] = True
        return True

    max_degree = 0
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            # (i, j)を捜索する
            if grid[i][j] == "#" and not can_start(i, j):
                visited[i][j] = True
                max_degree = max(max_degree, 1)
                grid_memo[i][j] = max_degree
                break

            elif grid[i][j] == "." and not visited[i][j] and can_start(i, j):
                stack = [(i, j)]
                visited[i][j] = True
                degree = 1

                while stack:
                    x, y = stack.pop()
                    if (
                        0 <= x < h
                        and 0 <= y < w
                        and not visited[i][j]
                        and grid_memo[x][y] is not None
                    ):
                        degree += grid_memo[x][y]
                        visited[x][y] = True
                        continue
                    degree += 1

                    if not can_start(x, y):
                        continue

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w:
                            if grid[nx][ny] == "." and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))

                max_degree = max(max_degree, degree)
                grid_memo[i][j] = degree

    print(max_degree)


if __name__ == "__main__":
    main()
