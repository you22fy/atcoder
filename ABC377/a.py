def main():
    s = input()
    ss = ''.join(sorted(list(s)))
    if ss == 'ABC':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
