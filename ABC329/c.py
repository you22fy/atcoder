# TLE
# n = int(input())
# s = input()

# substring = set()
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n +1):
#         w = s[i:j]
#         if not w in substring and len(set(w)) == 1:
#             ans += 1
#         substring.add(w)
# print(ans)

# n =  int(input())
# s = input()

# ans = 0
# i = 0
# last_count = dict()

# while i < n:
#     j = i
#     while j < n and s[i] == s[j]:
#         j += 1
#     length = j - i
#     prev_length = last_count.get(s[i], 0)
#     if length > prev_length:
#         ans += length - prev_length

#     last_count[s[i]] = length
#     i = j
# print(ans)


n = int(input())
s = input()

count = 0
i = 0

while i < n:
    char = s[i]
    length = 0

    while i < n and s[i] == char:
        i += 1
        length += 1

    count += length * (length + 1) // 2

print(count)
