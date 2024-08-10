"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n = int(input())
    s = input()

    win_map = {
        "P": "S",
        "R": "P",
        "S": "R",
    }

    me = ""
    prev = ""
    ans = 0
    for h in s:
        me = win_map[h]  # とりあえず勝っとく
        if me == prev:
            me = h  # あいこにする
        else:
            ans += 1
        prev = me

    print(ans)


if __name__ == "__main__":
    main()
