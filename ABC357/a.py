n,m = map(int, input().split())
h = list(map(int, input().split()))

hands_sum = 0
i = 0
for hi in h:
    hands_sum += hi
    if hands_sum > m:
        print(i)
        exit()
    i+= 1
print(i)
