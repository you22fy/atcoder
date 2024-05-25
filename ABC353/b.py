"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    left = k
    current_top_group = 0
    while current_top_group < n:
        if left < a[current_top_group]:
            # 空席がない場合->出発

            ans += 1
            left = k
        else:
            # 案内可能
            left -= a[current_top_group]
            # tmp.append(a[current_top_group])
            current_top_group += 1
    if left != k:  # 最後のグループが出発していない場合
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
