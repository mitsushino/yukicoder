import datetime

second_sum = 0
n = int(input())
for _ in range(n):
    time_list = input().split(' ')
    time1 = time_list[0].split(':')
    time2 = time_list[1].split(':')
    d1 = datetime.datetime(1900, 1, 1, int(time1[0]), int(time1[1]), 0)
    d2 = datetime.datetime(1900, 1, 1, int(time2[0]), int(time2[1]), 0)
    if d1 > d2:
        d2 = datetime.datetime(1900, 1, 2, int(time2[0]), int(time2[1]), 0)
    td = d2 - d1
    second_sum += td.seconds
print(second_sum // 60)
