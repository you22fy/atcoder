n,m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(m)]

check_list = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    check_list[i][i] = -1


for line in pic:
    for k in range(n-1):
        check_list[line[k]-1][line[k+1]-1] = 1
        check_list[line[k+1]-1][line[k] -1] = 1

count = 0
for relation in check_list:
    count += relation.count(0)
print(count//2)