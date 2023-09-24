import itertools

k = int(input())

candidate = []
numbers = tuple(range(10))

for i in range(11):
    for j in itertools.combinations(numbers, i):
        j = map(str, j)
        candidate.append("".join(sorted(j, reverse=True)))

candidate.remove('')
candidate.remove('0')
candidate = list(map(int, candidate))
candidate.sort()
print(candidate[k-1])