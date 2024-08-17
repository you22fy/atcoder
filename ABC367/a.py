"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    a, b, c = map(int, input().split())
    if b < c:  # 同じ日に寝て起きる場合
        print("Yes" if a < b or a >= c else "No")
    else:  # 日付をまたぐ場合
        print("Yes" if a < b and a >= c else "No")


if __name__ == "__main__":
    main()
