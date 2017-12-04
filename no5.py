wide_box_len = int(input())
box_numbers = int(input())
boxes = list(map(int, input().split()))
boxes.sort()
sum_box = 0

for box in boxes:
    wide_box_len -= box
    if wide_box_len >= 0:
        sum_box += 1
    else:
        break
print(sum_box)
