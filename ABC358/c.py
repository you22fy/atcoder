"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]  # n(店舗) * m(種類)

    full_mask = (1 << m) - 1

    masks = []
    for store in s:
        mask = 0
        for i, c in enumerate(store):
            if c == "o":
                mask |= 1 << i
        masks.append(mask)

    min_stores = float("inf")

    for i in range(1, 1 << n):
        combined_mask = 0
        store_count = 0
        for j in range(n):
            if i & (1 << j):
                combined_mask |= masks[j]
                store_count += 1

        if combined_mask == full_mask:
            min_stores = min(min_stores, store_count)
    print(min_stores)


if __name__ == "__main__":
    main()
