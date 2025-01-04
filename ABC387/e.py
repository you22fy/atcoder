import sys
sys.setrecursionlimit(10**8)

MAX_CHECK = 10**100000


def main():
    N_str = sys.stdin.readline().strip()

    N_int = int(N_str)
    twoN_int = N_int * 2
    twoN_str = str(twoN_int)

    def digit_sum(num_str):  # O(len(num_str))?
        return sum(map(int, num_str))

    def mod_int(num_str, k):
        r = 0
        for ch in num_str:
            r = (r * 10 + (ord(ch) - ord('0'))) % k
        return r

    def add_one(num_str):  # 1増やす,O(len(num_str))?
        arr = list(num_str)
        i = len(arr) - 1
        carry = 1
        while i >= 0 and carry > 0:
            x = (ord(arr[i]) - ord('0')) + carry
            carry = x // 10
            arr[i] = str(x % 10)
            i -= 1
        if carry > 0:
            arr.insert(0, '1')
        return "".join(arr)

    def compare_str(a_str, b_str):
        if len(a_str) < len(b_str):
            return -1
        elif len(a_str) > len(b_str):
            return 1
        else:
            if a_str < b_str:
                return -1
            elif a_str > b_str:
                return 1
            else:
                return 0

    def is_good_number(num_str):
        s = digit_sum(num_str)
        r = mod_int(num_str, s)
        return (r == 0)

    a_str = N_str

    a_str = N_str
    for _ in range(MAX_CHECK):
        if compare_str(a_str, twoN_str) > 0:
            break

        if is_good_number(a_str):
            a_plus_1 = add_one(a_str)
            if compare_str(a_plus_1, twoN_str) <= 0:
                if is_good_number(a_plus_1):
                    print(a_str.lstrip('0') or '0')  # ゼロ梅を消す
                    return
        a_str = add_one(a_str)

    print(-1)


if __name__ == '__main__':
    main()
