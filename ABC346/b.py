w, b = map(int, input().split())

s= "wbwbwwbwbwbw" * (max(w , b) + 1)


for i in range(len(s) - w -b + 1):
    substring = s[i:i+w+b]
    w_cnt = substring.count('w')
    b_cnt = substring.count('b')

    if w_cnt == w and b_cnt == b:
        print("Yes")
        exit()

print("No")


