n, m = map(int, input().split())
s = input()
t = input()
t_rev = t[::-1]
isPrefix = t[:n] == s
isSuffix = t_rev[:n] == s[::-1]
if isPrefix and isSuffix:
    print(0)
elif isPrefix and not isSuffix:
    print(1)
elif not isPrefix and isSuffix:
    print(2)
elif not isPrefix and not isSuffix:
    print(3)