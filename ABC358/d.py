"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, _ = map(int, input().split())
    a = list(map(int, input().split()))  # ai円でai個
    b = list(map(int, input().split()))  # 人iにbi個以上の箱渡す

    sorted_a = sorted(a)
    sorted_b = sorted(b)
    # print(sorted_a)
    # print(sorted_b)
    ans = 0
    cursor = 0
    for bi in sorted_b:
        while cursor < n and sorted_a[cursor] < bi:
            cursor += 1
        if cursor == n:
            print(-1)
            return
        ans += sorted_a[cursor]
        cursor += 1

    print(ans)



if __name__ == "__main__":
    main()
