n = int(input())
r = input()
c = input()

grid = [['.' for _ in range(n)] for _ in range(n)]

def show_grid():
    for row in grid:
        print(*row)

col_top = []
row_top = []

for i in range(n):
    for j in range(n):
        # col_topを埋める
        if i == 0:
            col_top.append()

