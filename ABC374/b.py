def main():
    s = input()
    t = input()

    if s == t:
        print(0)
        return

    if len(s) < len(t):
        s += '$' * (len(t) - len(s))
    elif len(t) < len(s):
        t += '$' * (len(s) - len(t))

    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            return

if __name__ == '__main__':
    main()
