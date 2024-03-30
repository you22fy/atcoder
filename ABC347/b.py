s = input()

ans = set()

# sの全ての部分文字列をasnに追加
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        ans.add(s[i:j])
print(len(ans))
