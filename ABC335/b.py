n = int(input())
ans = []
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i+j+k <= n:
                ans.append((i, j, k))
ans.sort()
for i, j, k in ans:
    print(f"{i} {j} {k}")

