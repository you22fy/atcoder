from itertools import chain, combinations

def main():
    n = int(input())
    k = list(map(int, input().split()))

    s = list(range(len(k)))
    ps = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    min_max_value = float('inf')
    for subset in ps:
        if len(subset) <= len(k) // 2:
            group1 = [k[i] for i in subset]
            group2 = [k[i] for i in range(len(k)) if i not in subset]
            if len(group1) == 0 or len(group2) == 0:
                continue
            min_max_value = min(min_max_value, max(sum(group1), sum(group2)))

    print(min_max_value)
if __name__ == '__main__':
    main()
