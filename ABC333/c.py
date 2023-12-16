n = int(input())
repunits = [int("1" * i) for i in range(1, 13)]
sums = set()

for i in repunits:
    for j in repunits:
        for k in repunits:
            sums.add(i + j + k)

sorted_sums = sorted(list(sums))

print(sorted_sums[n-1])