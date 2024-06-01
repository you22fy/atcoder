def max_min_ratio_sum(n, array):
    array.sort()
    total_sum = 0
    i = 0
    while i < n:
        # Count the frequency of the current element
        start = i
        while i < n and array[i] == array[start]:
            i += 1
        count = i - start

        # For each element at or after index i
        for j in range(i, n):
            quotient = array[j] // array[start]
            total_sum += quotient * count

    return total_sum


n = int(input())
array = list(map(int, input().split()))
result = max_min_ratio_sum(n, array)
print(result)
