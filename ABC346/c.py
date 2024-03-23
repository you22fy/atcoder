n, k = map(int, input().split())
a = list(map(int, input().split()))
set_a = set()
for a_i in a:
    if 1 <= a_i <= k:
        set_a.add(a_i)

sum_of_1_to_k = k * (k + 1) // 2
ans  = sum_of_1_to_k - sum(set_a)
print(ans)