import sys

sys.setrecursionlimit(10**9)


def main():
    s = int(input())
    if 200 <= s <= 299:
        print('Success')
    else:
        print('Failure')

if __name__ == '__main__':
    main()
