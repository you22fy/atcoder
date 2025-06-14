def main():
    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    boxId_to_ballCount = {i+1:0 for i in range(n)}

    for xi in x:
        if xi != 0:
            boxId_to_ballCount[xi] += 1
            print(xi, end=' ')
            continue

        min_box_id = min(boxId_to_ballCount, key=boxId_to_ballCount.get)
        boxId_to_ballCount[min_box_id] += 1
        print(min_box_id, end=' ')
    print()




if __name__ == "__main__":
    main()
