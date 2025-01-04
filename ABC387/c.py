from collections import defaultdict, deque


def dp_and_dfs(x: int) -> int:
    if x < 10:
        return 0

    digits = list(map(int, str(x)))
    n = len(digits)
    dp = defaultdict(int)
    queue = deque()

    start_state = (0, -1, True, True, 0)
    dp[start_state] = 1
    queue.append(start_state)

    ans = 0

    while queue:
        (pos, lead, is_tight, leading_zero, length) = queue.popleft()
        ways = dp[(pos, lead, is_tight, leading_zero, length)]

        if pos == n:
            if length >= 2:
                ans += ways
            continue

        limit = digits[pos] if is_tight else 9

        for d in range(limit + 1):
            next_is_tight = is_tight and d == limit

            if leading_zero:
                if d == 0:
                    nxt = (pos + 1, -1, next_is_tight, True, 0)
                else:
                    nxt = (pos + 1, d, next_is_tight, False, 1)
            else:
                if d < lead:
                    nxt = (pos + 1, lead, next_is_tight, False, length + 1)
                else:
                    continue

            if dp[nxt] == 0:
                queue.append(nxt)
            dp[nxt] += ways

    return ans


def main():
    l, r = map(int, input().split())
    print(dp_and_dfs(r) - dp_and_dfs(l - 1))


if __name__ == "__main__":
    main()
