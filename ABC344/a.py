s = input()
pos1, pos2 = None, None

for idx, c in enumerate(s):
    if c == '|':
        if pos1 == None:
            pos1 = idx
        else:
            pos2 = idx
ans = s[:pos1] + s[pos2+1:]
print(ans)