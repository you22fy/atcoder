from itertools import permutations
import math


def main():
    n, s, t = map(int, input().split())
    lines = [list(map(int, input().split())) for _ in range(n)]

    min_total_time = float('inf')

    for order in permutations(range(n)):
        for flip in range(1 << n):
            total_time = 0.0
            prev = (0, 0)
            for i, line_idx in enumerate(order):
                x1, y1, x2, y2 = lines[line_idx]
                if flip & (1 << i):
                    x1, y1, x2, y2 = x2, y2, x1, y1

                dx = prev[0] - x1
                dy = prev[1] - y1
                move_distance = math.hypot(dx, dy)
                total_time += move_distance / s

                dx = x2 - x1
                dy = y2 - y1
                draw_distance = math.hypot(dx, dy)
                total_time += draw_distance / t

                prev = (x2, y2)

            if total_time < min_total_time:
                min_total_time = total_time

    print(min_total_time)


if __name__ == '__main__':
    main()
