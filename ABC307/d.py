n = int(input())
s = input()

stack = []
ans = ""

for w in s:
    if w == "(":
        stack.append(len(ans))
        ans += w
    elif w == ")":
        if len(stack) >0:
            pos = stack.pop()
            ans = ans[:pos]
        else:
            ans += w
    else:
        ans += w
print(ans)
