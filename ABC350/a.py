def main():
    s = input()

    suffix = s[3:]

    if int(suffix) == 316:
        print("No")
        exit()

    if 0 < int(suffix) <= 349:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()