def main():
    n = int(input())
    s = [input() for _ in range(n)]

    is_logged_in = False
    fail_count = 0
    for si in s:
        match si:
            case 'login':
                is_logged_in = True
            case 'logout':
                is_logged_in = False
            case 'public':
                continue
            case 'private':
                if not is_logged_in:
                    fail_count += 1

    print(fail_count)
if __name__ == '__main__':
    main()
