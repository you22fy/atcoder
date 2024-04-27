"""python_template"""


def main():
    """main function"""
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * w for _ in range(h)]

    def can_start(x, y):
        """can_start"""
        if grid[x][y] == "#":
            return False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == "#":
                return False
        return True

    max_degree = 0

    for i in range(h):
        for j in range(w):
            # (i, j)を捜索する
            if grid[i][j] == "#" and not can_start(i, j):
                visited[i][j] = True
                max_degree = max(max_degree, 1)
                break

            if grid[i][j] == "." and not visited[i][j] and can_start(i, j):
                stack = [(i, j)]
                visited[i][j] = True
                degree = 1

                while stack:
                    x, y = stack.pop()
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

    print(max_degree)


if __name__ == "__main__":
    main()
