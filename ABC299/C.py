n = int(input())
s = input()
mx = 0
t = 0
for i in range(n-1):
    if s[i] == s[i+1] and s[i] != '-':
        t += 1
    else:
        mx = max(mx, t)
print(mx)