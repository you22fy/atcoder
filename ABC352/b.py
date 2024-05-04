"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""

    s = input()
    t = input()

    len_s = len(s)
    i = 0
    ans = []
    for idx, c in enumerate(t):
        # print(c, s[i])
        if c == s[i]:
            # print('true')
            i += 1
            ans.append(str(idx + 1))
            if i == len_s:
                break
    print(*ans)
if __name__ == "__main__":
    main()
