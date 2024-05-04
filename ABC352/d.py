"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, k = map(int, input().split())
    p_lst = list(map(int, input().split()))
    ans = float("inf")

    p_val_idx = {}
    for idx, p in enumerate(p_lst):
        p_val_idx[p] = idx + 1  # 1-indexed
    print(p_val_idx)

    for i in range(k, n + 1):
        ps, pe = i - (k - 1), i  # ps <= pi <= pe の範囲で探す
        # print(ps, pe)

        # 良い添字列かどうかを判定する
        valid = True
        prev_idx = p_val_idx[ps]  # 最初の値のインデックス
        # print('start')
        for p_val in range(ps + 1, pe + 1):
            cur_idx = p_val_idx[p_val]
            # print(cur_idx, prev_idx)
            if cur_idx < prev_idx:
                # print('out', cur_idx, prev_idx)
                valid = False
                break
            prev_idx = cur_idx

        if not valid:
            continue

        diff = p_val_idx[pe] - p_val_idx[ps]
        ans = min(ans, diff)

    print(ans)
    return


if __name__ == "__main__":
    main()
