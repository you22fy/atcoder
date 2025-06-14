def main():
    x = int(input())
    s = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i* j == x:
                continue
            s += i*j
    print(s)

if __name__ == "__main__":
    main()
