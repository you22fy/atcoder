A, M, L, R = map(int, input().split())
if (L - A) % M == 0:
    first_tree = L
else:
    first_tree = L + (M - (L - A) % M)

last_tree = R - (R - A) % M

if first_tree > R or last_tree < L:
    print(0)
else:
    print((last_tree - first_tree) // M + 1)

