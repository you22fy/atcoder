"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, k = map(int, input().split())
    s = list(input())
    count = 0


    def non_palindromic_count(sub):
        length = len(sub)
        half = length // 2
        changes_needed = 0

        for i in range(half):
            left = sub[i]
            right = sub[length - i - 1]
            if left == "?" and right == "?":
                changes_needed += 2
            elif left == "?":
                changes_needed += 1
            elif right == "?":
                changes_needed += 1
            elif left != right:
                changes_needed += 0
            else:
                return 0
        ans = 2 ** (changes_needed - half)
        print(ans % 998244353)
        exit()
    for i in range(n - k + 1):
        substring = s[i : i + k]
        count += non_palindromic_count(substring)

    print(count % 998244353)


if __name__ == "__main__":
    main()
