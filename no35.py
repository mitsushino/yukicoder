if __name__ == '__main__':
    N = int(input())
    correct_type_sum = 0
    missed_type_sum = 0
    for _ in range(N):
        ts = input().split()
        t = int(ts[0])
        s = len(ts[1])
        type_num = int(12 * t / 1000)
        if type_num > s:
            correct_type_sum += s
        else:
            correct_type_sum += type_num
        missed_type = s - type_num
        if missed_type > 0:
            missed_type_sum += missed_type
    print(correct_type_sum, missed_type_sum)
