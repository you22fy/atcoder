"""python_template"""

# NOTE: GIVE UP
import sys

sys.setrecursionlimit(10**9)
MOD = 998244353
ASCII_A = 97

def main():
    """main function"""
    k = int(input())  # 1 <= k <= 1000
    c = list(map(int, input().split()))

    # 利用可能な文字とその最大使用回数をマップに格納
    available_char_count_map = {chr(i + ASCII_A): c[i] for i in range(len(c)) if c[i] > 0}
    all_char_count = sum(available_char_count_map.values())
    char_kind_count = len(available_char_count_map.keys())
    k = max(k , all_char_count)
    for use_k in range(1, k + 1):
        # 使う文字の組み合わせを求める
        for char in available_char_count_map.keys():
            pass

if __name__ == "__main__":
    main()
