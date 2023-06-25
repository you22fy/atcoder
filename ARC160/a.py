n , k = map(int, input().split())
lst = list(map(int, input().split()))
keys = []
for i_l in range(1, n+1):
    for i_r in range(1, n+1):
        if i_l <= i_r:
            keys.append((i_l, i_r))


def make_rev_numbers(l, r):
    left_part = lst[:l]
    before_rev = lst[l:r+1]
    rev = before_rev[::-1]
    right_part = lst[r+1:]
    ret = left_part + rev + right_part
    return ret


nums = []
for pair in keys:
    rev_lst = make_rev_numbers(pair[0]-1, pair[1]-1)
    cat_num = int(''.join(map(str, rev_lst)))
    nums.append([cat_num, rev_lst, ] )

sorted_nums = sorted(nums,  key=lambda x: x[0])
print(*sorted_nums[k-1][1])

