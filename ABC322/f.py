def c1(li, ri):
    for i in range(li-1, ri):
        if s[i] == '0':
            s[i] = '1'
        elif s[i] == '1':
            s[i] = '0'

def c2(li, ri):
    maxCount = 0
    current_count = 0
    for char in s[li-1: ri]:
        if char == '1':
            current_count += 1
            maxCount = max(maxCount, current_count)
        else:
            current_count = 0
    return maxCount

if __name__ == '__main__':
    n, q = map(int, input().split())
    s = list(input())
    queries = []
    for _ in range(q):
        c, l, r = map(int, input().split())
        if c == 1:
            c1(l,r)
        else:
            print(c2(l,r))

