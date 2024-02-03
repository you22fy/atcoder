n = int(input())
a = list(map(int, input().split()))
needed_people = 0
min_people = 0

for dif in a:
    min_people += dif
    if min_people < 0:
        needed_people += abs(min_people)
        min_people = 0

print(sum(a) + needed_people)