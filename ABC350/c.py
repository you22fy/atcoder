def main():
    N = int(input())
    A = list(map(int, input().split()))

    operations = []
    A = [0] + A
    for i in range(1, N + 1):
        while A[i] != i:
            j = A[i]
            A[i], A[j] = A[j], A[i]
            operations.append((i, j))

    print(len(operations))
    for op in operations:
        print(op[0], op[1])


if __name__ == '__main__':
    main()

