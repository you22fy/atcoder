n,m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))

for i in range(m):
    p = []
    p_word = []
    for j_id, j in enumerate(c):
        if j == i+1:
            p.append(j_id)
            p_word.append(s[j_id])
    p_word = p_word[-1:]+p_word[:-1]
    for k_id, k in enumerate(p):
        s[k] = p_word[k_id]

print("".join(s))