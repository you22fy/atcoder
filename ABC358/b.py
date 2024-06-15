"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    _, a = map(int, input().split())
    t = list(map(int, input().split()))
    end_time = 0

    for arrival_time in t:
        start_time = max(arrival_time, end_time)
        end_time = start_time + a
        print(end_time)


if __name__ == "__main__":
    main()
