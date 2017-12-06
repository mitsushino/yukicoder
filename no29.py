# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(input())
    item_list = []
    for _ in range(N):
        item_list.extend(list(map(int, input().split())))
    powerup_count = 0
    i = 0
    while i < len(item_list):
        num = item_list[i]
        if item_list.count(num) > 1:
            item_list.remove(num)
            item_list.remove(num)
            powerup_count += 1
            i = 0
        else:
            i += 1
    powerup_count += len(item_list) // 4
    print(powerup_count)
