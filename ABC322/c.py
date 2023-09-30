n, m = map(int, input().split())
a = list(input().split())
stack = []
for i in range(m-1, -1, -1):
    stack.append(int(a[i]))
for j in range(n):
    if j + 1 == stack[-1]:
        print(0)
        stack.pop()

    else:
        print(stack[-1] - (j+1))
