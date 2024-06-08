"""久しぶりにGPTなしでD解けたわ〜い"""


def pow_mod(base, exp, mod):
    """
    高速累乗法
    link : https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
    link : https://qiita.com/b1ueskydragon/items/0b8e0c382d782423c6d3
    """
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def geometric_series_sum(a, r, n, mod):
    """
    等比数列の和
    """
    if r == 1:
        return (a * n) % mod
    else:
        r_pow_n = pow_mod(r, n, mod)
        r_minus_1_inv = pow_mod(r - 1, mod - 2, mod)
        return (a * ((r_pow_n - 1 + mod) % mod) % mod) * r_minus_1_inv % mod


def main():
    """"""
    n = int(input())
    mod = 998244353
    len_n = len(str(n))
    r = pow_mod(10, len_n, mod)

    res = geometric_series_sum(n % mod, r, n, mod)
    print(res)


if __name__ == "__main__":
    main()
