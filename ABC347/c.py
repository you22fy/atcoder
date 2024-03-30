# これはTLE
# n, a, b = map(int, input().split())

# d = list(map(int, input().split()))

# for today in range(1, 1 + a + b):
#     is_all_day_valid = True
#     for event_day in d:
#         if not(1 <= (today + event_day) % (a + b) <= a):
#             is_all_day_valid = False
#             break
#     if is_all_day_valid:
#         print("Yes")
#         exit()
# print("No")


N, A, B = map(int, input().split())
D = [int(i) % (A + B) for i in input().split()]
D = sorted(set(D))

if len(D) == 1:
    print('Yes')
else:
    for i in range(len(D)):
        if (D[(i + 1) % len(D)] - D[i]) % (A + B) > B:
            print('Yes')
            break
    else:
        print('No')