n = int(input())
s = set()
s_rev = set()
for _ in range(n):
    inp = input()
    s.add(min(inp, inp[::-1]))
print(len(s))
