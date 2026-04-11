def main():
	n = int(input())
	s = input()
	i = 0
	while s[i] == 'o':
		i += 1
		if i >= len(s):
			break
	print(s[i:])

if __name__ == "__main__":
	main()

