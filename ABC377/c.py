def main():
    n, m = map(int, input().split())
    knights = [list(map(int, input().split())) for _ in range(m)]

    answer = n * n
    targets_set = set()
    for k in knights:
        targets_set.add((k[0], k[1]))

    for xi, yi in knights:
        targets_set |= get_valid_targets(n, xi, yi)

    print(answer - len(targets_set))


def get_valid_targets(n: int, x: int, y: int) -> set:
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    ret = set()

    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy

        if 1 <= new_x <= n and 1 <= new_y <= n:
            ret.add((new_x, new_y))

    return ret


if __name__ == '__main__':
    main()
