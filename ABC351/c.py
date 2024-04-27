"""python_template"""


def main():
    """main function"""
    _ = int(input())
    a = list(map(int, input().split()))

    seq = []
    for power in a:
        seq.append(power)
        while len(seq) > 1 and seq[-2] == seq[-1]:
            i, _ = seq.pop(), seq.pop()
            # print(i)
            seq.append(i + 1)
    print(len(seq))


if __name__ == "__main__":
    main()
