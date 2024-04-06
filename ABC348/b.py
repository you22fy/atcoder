n = int(input())

positions = [tuple(map(int, input().split())) for _ in range(n)]

distances = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        dis = abs((positions[i][0] - positions[j][0]) ** 2) + abs((positions[i][1] - positions[j][1]) ** 2)
        distances[i][j] = dis
        distances[j][i] = dis
# print(distances)

for i in range(n):
    mn = max(distances[i])
    # print(f'mn : {mn}')
    for j in range(n):
        if distances[i][j] == mn:
            print(j + 1)
            break