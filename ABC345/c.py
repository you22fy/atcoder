s = list(input())
n = len(s)

total_patterns = n * (n - 1) //2

for i in set(s):
    cnt = s.count(i)
    if cnt > 1:
        continue

    same = cnt * (cnt - 1) // 2
    if same == 1:
        total_patterns -= 1
    else:
        total_patterns -= (same -1)
print(total_patterns)