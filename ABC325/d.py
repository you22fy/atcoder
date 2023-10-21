n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]

sorted_pairs = sorted(pairs, key=lambda x : x[1], reverse=True)
ans = n

for i in range(1,n):
    if sorted_pairs[i][0] < sorted_pairs[i-1][1]:
        sorted_pairs[i][1] = sorted_pairs[i-1][1]
        ans -=1
print(ans)
