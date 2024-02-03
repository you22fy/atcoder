h, w, n = map(int, input().split())

grid = [['.' for _ in range(w)] for _ in range(h)]

directions_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
current_direction_key = 0
row, col = (0, 0)

for i in range(n):
    # if not (0 <= row < h and 0 <= col < w):
    #     continue

    if grid[row][col] == '.':
        grid[row][col] = '#'
    else:
        grid[row][col] = '.'
    current_direction_key = (
        current_direction_key + 1) % 4 if grid[row][col] == '#' else (current_direction_key - 1) % 4
    row, col = (row + directions_dict[current_direction_key][0]
                ) % h, (col + directions_dict[current_direction_key][1]) % w


for r in grid:
    print(''.join(r))
