def main():
    s = input()
    if len(s) < 3:
        print("No")
        return
    last_three = s[-3:]
    if last_three == 'san':
        print("Yes")
        return
    print("No")
    return


if __name__ == '__main__':
    main()
