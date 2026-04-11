def main():
	n = int(input())
	l = list(map(int, input().split()))

	ans = 0
	for i in range(1 << n):
		passed, pos = 0, 0.5
		for j in range(n):
			prev = pos
			if (i >> j) & 1 == 1:
				pos -= l[j]
			else:
				pos += l[j]
			
			if prev * pos < 0:
				passed += 1
		ans = max(ans, passed)
	print(ans)

if __name__ == "__main__":
	main()

