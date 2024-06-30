"""python_template"""


def main():
    """main function"""
    n = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    box_items_map = {i: [] for i in range(n)}
    for ai, wi in zip(a, w):
        box_items_map[ai - 1].append(wi)

    ans = 0
    for values in box_items_map.values():
        if len(values) <= 1:
            continue
        values.sort()
        ans += sum(values[:-1])
    print(ans)


if __name__ == "__main__":
    main()
