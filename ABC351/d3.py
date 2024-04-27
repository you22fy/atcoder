import sys

sys.setrecursionlimit(10**9)

A = 1


def dfs(x, y):
    global B
    # 今いるところを W に置き換える
    field[x][y] = "W"

    # 移動する8方向をループ
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        # x, y 方向それぞれに dx, dy 移動した場所を (nx, ny) とする
        nx = x + dx
        ny = y + dy

        # nx と ny が庭の範囲内かどうか
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if field[nx][ny] == ".":
                B += 1
                # print("ok", B, nx, ny)

                dfs(nx, ny)
            elif (
                field[nx][ny] != "#"
                and field[nx][ny] != "W"
                and field[nx][ny] != str(i) + str(j)
            ):
                B += 1
                field[nx][ny] = str(i) + str(j)
                # print("stop",B, nx,ny,field[nx][ny])


n, m = map(int, input().split())
field = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if field[i][j] == ".":
            if i >= 1 and field[i - 1][j] == "#":
                field[i][j] = "S"
            if i < n - 1 and field[i + 1][j] == "#":
                field[i][j] = "S"
            if j >= 1 and field[i][j - 1] == "#":
                field[i][j] = "S"
            if j < m - 1 and field[i][j + 1] == "#":
                field[i][j] = "S"
# print(field)

for i in range(n):
    for j in range(m):
        if field[i][j] == ".":
            B = 1
            dfs(i, j)
            A = max(A, B)
            # print(B,i,j)
            # for _ in field:
            # print(_)
# print(B)
print(A)
