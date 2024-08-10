"""python_template"""

import sys

sys.setrecursionlimit(10**9)


# def main():
#     N = int(input())
#     A = list(map(int, input().split()))

#     # 累積XORを計算（0-based index）
#     xor_cumsum = [0] * (N + 1)
#     for i in range(N):
#         xor_cumsum[i + 1] = xor_cumsum[i] ^ A[i]

#     ans = 0
#     for i in range(N):
#         for j in range(i + 1, N):
#             ans += xor_cumsum[j + 1] ^ xor_cumsum[i]

#     print(ans)


# if __name__ == "__main__":
#     main()
def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for bit in range(30):
        count = [0, 0]
        current = 0
        for i in range(N):
            current ^= (A[i] >> bit) & 1
            count[current] += 1

        total = count[1] * (count[1] - 1) // 2 + count[0] * count[1]
        if total % 2 == 1:
            ans |= 1 << bit

    print(ans)


if __name__ == "__main__":
    main()
