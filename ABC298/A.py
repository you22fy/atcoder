# # shortest
# n = int(input())
# s = input()
# print('Yes' if 'o' in s and not'x' in s else 'No')

# # ex1
# n = int(input())
# s = input()

# if 'o' in s and not'x' in s:
#     print('Yes')
# else:
#     print('No')

# # ex2
# # input
# n = int(input())
# s = input()

# # flagを準備
# o_flag = False
# x_flag = False

# for i in s:
#     if i == 'o':
#         o_flag = True
#     if i == 'x':
#         x_flag = True
# if o_flag and not x_flag:
#     print('Yes')
# else:
#     print('No')

# ex3
n = int(input())
s = input()

s = s.replace('-','')
s_lst = list(s)
s_set = set(s_lst)