"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    s = input()
    upper_cnt = 0
    lower_cnt = 0

    for si in s:
        if si.isupper():
            upper_cnt += 1
        else:
            lower_cnt += 1
    if upper_cnt > lower_cnt:
        print(s.upper())
    else:
        print(s.lower())


if __name__ == "__main__":
    main()
