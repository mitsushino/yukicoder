# def cnt_delete(s):
#     original_s = s
#     left_cnt = 0
#     while True:
#         if 'ccw' in s:
#             s = s[1:]
#             left_cnt += 1
#         else:
#             break
#
#     right_cnt = 0
#     s = original_s
#     while True:
#         if 'ccw' in s:
#             s = s[:-1]
#             right_cnt += 1
#         else:
#             break
#     if left_cnt < right_cnt:
#         print(left_cnt)
#     else:
#         print(right_cnt)

from collections import Counter

s = Counter(list(input()))
print(min(s['c'] - 1, s['w']))


# cnt_delete(s)
