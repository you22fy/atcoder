"""python_template"""


def main():
    """main function"""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sa = sum(a)
    sb = sum(b)
    print(sa - sb + 1)


if __name__ == "__main__":
    main()
