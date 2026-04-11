def main():
	t,x = map(int ,input().split())
	a = list(map(int, input().split()))
	latest: int
	logs = []
	for i, ai in enumerate(a):
		if i == 0:
			val = ai
			logs.append((i, ai))
			continue
		
		if abs(val - ai) >= x:
			val = ai
			logs.append((i, ai))
	for log in logs:
		print(log[0], log[1])

	
	

if __name__ == "__main__":
	main()
