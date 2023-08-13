def rotate_string(n, m, s, c):
    # Create a dictionary to group indices
    indices_dict = {}
    for i, idx in enumerate(c):
        if idx in indices_dict:
            indices_dict[idx].append(i)
        else:
            indices_dict[idx] = [i]

    # For each unique index in c, rotate the characters
    for idx, positions in indices_dict.items():
        chars = [s[i] for i in positions]
        for i, pos in enumerate(positions):
            s = s[:pos] + chars[i-1] + s[pos+1:]
    
    return s

n,m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))

print(rotate_string(n, m, s, c)
)
