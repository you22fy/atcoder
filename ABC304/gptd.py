w, h = map(int, input().split())
n = int(input())

fruits_pos = [[0]*(w+1) for _ in range(h+1)]

for _ in range(n):
    x, y = map(int, input().split())
    fruits_pos[y][x] += 1

# 二次元累積和を計算
for i in range(h+1):
    for j in range(w+1):
        if i > 0:
            fruits_pos[i][j] += fruits_pos[i-1][j]
        if j > 0:
            fruits_pos[i][j] += fruits_pos[i][j-1]
        if i > 0 and j > 0:
            fruits_pos[i][j] -= fruits_pos[i-1][j-1]

a = int(input())
cut_y = [0]
cut_y += list(map(int, input().split()))
cut_y += [w]

b = int(input())
cut_x = [0]
cut_x += list(map(int, input().split()))
cut_x += [h]

cur_min = float('inf')
cur_max = 0

for i in range(b+1):
    for j in range(a+1):
        tmp = fruits_pos[cut_x[i+1]][cut_y[j+1]] - fruits_pos[cut_x[i+1]][cut_y[j]] - fruits_pos[cut_x[i]][cut_y[j+1]] + fruits_pos[cut_x[i]][cut_y[j]]
        cur_min = min(cur_min, tmp)
        cur_max = max(cur_max, tmp)
        
print("{} {}".format(cur_min, cur_max))
