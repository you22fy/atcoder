"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    s, t = input().split()
    for w in range(1, len(s) - 1):

        div_s = [s[i : i + w] for i in range(0, len(s), w)]
        max_len = max(list(map(len, div_s)))
        for c in range(max_len):
            tmp = "".join(list(map(lambda x: x[c] if c < len(x) else "", div_s)))
            if tmp == t:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
