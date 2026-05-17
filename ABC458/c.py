def main():
    s = input()
    c_idx = []
    for i, si in enumerate(s):
        if si == "C":
            c_idx.append(i)

    ans = 0
    for ci in c_idx:
        max_len = min(len(s) - ci - 1, ci)
        ans += max_len + 1
    
    print(ans)

if __name__ == "__main__":
    main()
