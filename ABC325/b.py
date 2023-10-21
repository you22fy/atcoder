n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
hours = [i + 1 for i in range(24)]
ans = 0
h = 0
for start_time in hours:
    end_time = start_time + 1
    tmp = 0
    for l in lst:

        if 9 <= (l[1] + start_time) % 24 <= 18 and 9 <= (l[1] + end_time) % 24 <= 18:
            tmp += l[0]
    if ans < tmp :
        ans = tmp
print(ans)