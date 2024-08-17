"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    total_distance = sum(a)
    ped_sum = [0] * (n + 1)
    for i in range(n):
        ped_sum[i + 1] = (ped_sum[i] + a[i]) % m

    remainders = [0] * m
    for ps in ped_sum:
        remainders[ps] += 1

    count = 0
    for r in remainders:
        count += r * (r - 1)

    if total_distance % m == 0:
        count += n

    print(count)


if __name__ == "__main__":
    main()
