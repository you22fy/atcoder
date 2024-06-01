"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = [list(map(int, input().split())) for _ in range(n)]

    nutrient_need_map = {k: v for k, v in enumerate(a)}
    nutrient_ate_map = {k: 0 for k in range(len(a))}

    for xi in x:
        for idx, nutrient in enumerate(xi):
            nutrient_ate_map[idx] += nutrient

    ans = True
    for idx, nutrient in nutrient_ate_map.items():
        if nutrient < nutrient_need_map[idx]:
            ans = False
            break

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
