def main():
    N, Q = map(int, input().split())

    pos = list(range(N + 1))
    occ = [0] * (N + 1)
    for i in range(1, N + 1):
        occ[i] = 1

    multiple = 0

    out_lines = []

    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            P = int(query[1])
            H = int(query[2])

            current_nest = pos[P]
            if occ[current_nest] == 2:
                multiple -= 1
            occ[current_nest] -= 1

            occ[H] += 1
            if occ[H] == 2:
                multiple += 1
            pos[P] = H

        else:
            out_lines.append(str(multiple))
    print("\n".join(out_lines))


if __name__ == '__main__':
    main()
