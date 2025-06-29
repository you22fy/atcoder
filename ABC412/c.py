def bin_search(a, t):
    low, high = 0, len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] <= t:
            low = mid + 1
        else:
            high = mid
    return low


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        N = int(input())
        S = list(map(int, input().split()))

        S_1 = S[0]
        S_N = S[N-1]

        if S_1 * 2 < S_N:
            middle_dominos = []
            for i in range(1, N-1):
                middle_dominos.append(S[i])
            middle_dominos.sort()

            current_size = S_1
            cnt = 1

            while current_size * 2 < S_N:
                idx = bin_search(middle_dominos, current_size * 2)

                if idx == 0:
                    cnt = -1
                    break

                next_ = middle_dominos[idx-1]
                if next_ <= current_size:
                    cnt = -1
                    break

                current_size = next_
                cnt += 1

            if cnt != -1 and current_size * 2 >= S_N:
                cnt += 1
            else:
                cnt = -1
        else:
            cnt = 2

        ans.append(cnt)

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
