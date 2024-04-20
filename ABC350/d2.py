from collections import defaultdict

def main():
    N, M = map(int, input().split())
    friendships = [tuple(map(int, input().split())) for _ in range(M)]

    friends = defaultdict(set)

    for A, B in friendships:
        friends[A].add(B)
        friends[B].add(A)

    operations = 0

    for X in range(1, N + 1):
        for Y in friends[X]:
            if X < Y:
                for Z in friends[X]:
                    if Z != Y and Z not in friends[Y]:
                        operations += 1
                        friends[Y].add(Z)
                        friends[Z].add(Y)
    print(operations)

if __name__ == '__main__':
    main()
