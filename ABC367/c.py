"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, k = map(int, input().split())
    r = list(map(int, input().split()))

    def generate_sequences(index, current_sum, sequence):
        if index == n:
            if current_sum % k == 0:
                print(*sequence)
            return

        for i in range(1, r[index] + 1):
            new_sequence = sequence + [i]
            new_sum = current_sum + i
            generate_sequences(index + 1, new_sum, new_sequence)

    generate_sequences(0, 0, [])


if __name__ == "__main__":
    main()
