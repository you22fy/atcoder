def min_time_to_match(s1, s2, s3, m):
    if m != len(s2) or m != len(s3):
        return -1
    s_intersection = set(s1).intersection(set(s2)).intersection(set(s3))

    min_time = float('inf')
    for symbol in s_intersection:
        if symbol in s1 and symbol in s2 and symbol in s3:
            for i in range(m):
                for j in range(m):
                    for k in range(m):
                        stop_s1 = i
                        stop_s2 = j
                        stop_s3 = k
                        total_time = max(stop_s1, stop_s2, stop_s3)
                        if s1[stop_s1 % m] == s2[stop_s2 % m] == s3[stop_s3 % m] == symbol:
                            min_time = min(min_time, total_time)

    return min_time if min_time != float('inf') else -1


if __name__ == "__main__":

    m = int(input())
    s1 = list(input())
    s2 = list(input())
    s3 = list(input())
    print(min_time_to_match(s1, s2, s3, m))
