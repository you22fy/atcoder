n = int(input())
slimes_info_dict = { }
for _ in range(n):
    k,v = map(int, input().split())
    slimes_info_dict[k] = v


# keyでソート
slimes_info_dict_sorted_by_key = dict(sorted(slimes_info_dict.items(), key=lambda x : x[0]))
slimes_info_dict_sorted_by_key_for_change = slimes_info_dict_sorted_by_key.copy()

def canMoreMerge(d):
    for v in d.values():
        if v > 1:
            return True
    return False


while True:
    for k, v in slimes_info_dict_sorted_by_key.items():
        if v >1:
            generated_slimes_num = v//2
            merged_slimes_size = v*2
            remain_slimes_num = v%2

            slimes_info_dict_sorted_by_key_for_change[k] = remain_slimes_num

            if merged_slimes_size in slimes_info_dict_sorted_by_key_for_change.keys():
                slimes_info_dict_sorted_by_key_for_change[merged_slimes_size] += generated_slimes_num
            else:
                slimes_info_dict_sorted_by_key_for_change[merged_slimes_size] = generated_slimes_num
    if canMoreMerge(slimes_info_dict_sorted_by_key_for_change):
        slimes_info_dict_sorted_by_key = slimes_info_dict_sorted_by_key_for_change.copy()
        slimes_info_dict_sorted_by_key_for_change = slimes_info_dict_sorted_by_key.copy()
    else:
        print(sum(slimes_info_dict_sorted_by_key_for_change.values()))
        exit()