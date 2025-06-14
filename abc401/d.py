def main():
    n, k = map(int, input().split())
    s_list = list(input())

    INF = n + 1
    NEG_INF = -1

    min_k_f = [[INF] * 2 for _ in range(n + 2)]
    max_k_f = [[NEG_INF] * 2 for _ in range(n + 2)]

    min_k_b = [[INF] * 2 for _ in range(n + 2)]
    max_k_b = [[NEG_INF] * 2 for _ in range(n + 2)]

    min_k_f[0][0] = 0
    max_k_f[0][0] = 0

    for i in range(1, n + 1):
        char = s_list[i-1]

        if char == '.' or char == '?':
            min_prev = INF
            max_prev = NEG_INF
            if min_k_f[i-1][0] != INF:
                min_prev = min(min_prev, min_k_f[i-1][0])
                max_prev = max(max_prev, max_k_f[i-1][0])
            if min_k_f[i-1][1] != INF:
                min_prev = min(min_prev, min_k_f[i-1][1])
                max_prev = max(max_prev, max_k_f[i-1][1])

            if min_prev != INF:
                min_k_f[i][0] = min_prev
                max_k_f[i][0] = max_prev

        if char == 'o' or char == '?':
            if min_k_f[i-1][0] != INF:
                min_k_f[i][1] = min_k_f[i-1][0] + 1
                max_k_f[i][1] = max_k_f[i-1][0] + 1

    min_k_b[n+1][0] = 0
    max_k_b[n+1][0] = 0

    for i in range(n, 0, -1):
        char = s_list[i-1]

        if char == '.' or char == '?':
            min_next = INF
            max_next = NEG_INF
            if min_k_b[i+1][0] != INF:
                min_next = min(min_next, min_k_b[i+1][0])
                max_next = max(max_next, max_k_b[i+1][0])
            if min_k_b[i+1][1] != INF:
                min_next = min(min_next, min_k_b[i+1][1])
                max_next = max(max_next, max_k_b[i+1][1])

            if min_next != INF:
                min_k_b[i][0] = min_next
                max_k_b[i][0] = max_next

        if char == 'o' or char == '?':
            if min_k_b[i+1][0] != INF:
                min_k_b[i][1] = min_k_b[i+1][0] + 1
                max_k_b[i][1] = max_k_b[i+1][0] + 1

    ans = [''] * n
    for i in range(1, n + 1):
        original_char = s_list[i-1]
        can_be_dot = False
        can_be_o = False

        if original_char == '.' or original_char == '?':
            for prev_state in range(2):
                for next_state in range(2):
                    min_f = min_k_f[i-1][prev_state]
                    max_f = max_k_f[i-1][prev_state]
                    min_b = min_k_b[i+1][next_state]
                    max_b = max_k_b[i+1][next_state]

                    if min_f != INF and min_b != INF:
                        min_total = min_f + min_b
                        max_total = max_f + max_b
                        if min_total <= k <= max_total:
                            can_be_dot = True
                            break
                if can_be_dot:
                    break

        if original_char == 'o' or original_char == '?':
            min_f = min_k_f[i-1][0]
            max_f = max_k_f[i-1][0]
            min_b = min_k_b[i+1][0]
            max_b = max_k_b[i+1][0]

            if min_f != INF and min_b != INF:
                min_total = min_f + 1 + min_b
                max_total = max_f + 1 + max_b
                if min_total <= k <= max_total:
                    can_be_o = True

        if original_char == '.':
            ans[i-1] = '.'
        elif original_char == 'o':
            ans[i-1] = 'o'
        elif original_char == '?':
            if can_be_dot and can_be_o:
                ans[i-1] = '?'
            elif can_be_dot:
                ans[i-1] = '.'
            elif can_be_o:
                ans[i-1] = 'o'

    print("".join(ans))


if __name__ == "__main__":
    main()
