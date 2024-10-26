def main():
    s = [list(input()) for _ in range(8)]
    invalid_rows = set()
    invalid_cols = set()

    for i in range(8):
        for j in range(8):
            if s[i][j] == '#':
                invalid_rows.add(i)
                invalid_cols.add(j)

    valid_rows = 8 - len(invalid_rows)
    valid_cols = 8 - len(invalid_cols)

    print(valid_rows * valid_cols)


if __name__ == '__main__':
    main()
