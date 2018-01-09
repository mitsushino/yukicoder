# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(input())
    _ = input()
    number_list = []
    for _ in range(N):
        number_list.append(int(input()))
    max_value = max(number_list)
    min_value = min(number_list)
    print(max_value - min_value)
