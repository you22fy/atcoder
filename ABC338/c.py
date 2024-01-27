n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

max_a = float("inf")
max_b = float("inf")

for q_i, a_i, b_i in zip(q, a, b):
    if a_i > 0:
        max_a = min(max_a, q_i // a_i)
    if b_i > 0:
        max_b = min(max_b, q_i // b_i)
max_combined = 0
for i in range(max_a + 1):
    remaining_q = [q[j] - i * a[j] for j in range(n)]
    max_b_with_a = float('inf')
    for j in range(n):
        if b[j] > 0:
            max_b_with_a = min(max_b_with_a, remaining_q[j] // b[j])
    max_combined = max(max_combined, i + max_b_with_a)

print(max_combined)
