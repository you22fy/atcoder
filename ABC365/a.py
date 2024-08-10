"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    y = int(input())
    if is_leap_year(y):
        print("366")
    else:
        print("365")


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
