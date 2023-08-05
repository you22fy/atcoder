n = int(input())
lst = list(map(int, input().split()))
if len(lst) == 1:
    print(0)
    exit()
f = lst[0]
candidate = lst[1:n-1]
strongest = max(candidate)
if f > strongest:
    target = f
else:
    target = strongest+1
print(target - lst[0])

