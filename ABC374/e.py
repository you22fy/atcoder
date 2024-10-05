import math


def div_ceil(a, b):
    return (a + b - 1) // b


def solve(n, x, a, p, b, q):
    l, r = 1, 1000000007
    while l <= r:
        te = (l + r) // 2
        rem = x

        for i in range(n):
            sub = float('inf')
            for j in range(b[i] + 1):
                cur = j * p[i]
                rte = max(0, te - a[i] * j)
                cur += div_ceil(rte, b[i]) * q[i]

                sub = min(sub, cur)
            for j in range(a[i] + 1):
                cur = j * q[i]
                rte = max(0, te - b[i] * j)
                cur += div_ceil(rte, a[i]) * p[i]

                sub = min(sub, cur)
            rem -= sub
            if rem < 0:
                break

        if rem >= 0:
            l = te + 1
        else:
            r = te - 1
    return r


def main():
    n, x = map(int, input().split())
    a, p, b, q = [], [], [], []
    for _ in range(n):
        ai, pi, bi, qi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        b.append(bi)
        q.append(qi)

    print(solve(n, x, a, p, b, q))


if __name__ == "__main__":
    main()
