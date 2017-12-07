# -*- coding: utf-8 -*-

import sys


def make_one_count_of_binary_digit(N):
    l = []
    for i in range(0, N + 1):
        l.append(bin(i).count('1'))
    return l


def move_idx(p_list, idx, N):
    p_list[idx]['right_move'] = True
    if idx + binary_digit_one_list[idx] <= N:
        return p_list, idx + binary_digit_one_list[idx]
    p_list[idx]['left_move'] = True
    return p_list, idx - binary_digit_one_list[idx]


if __name__ == '__main__':
    N = int(input())
    possibility_list = [{'left_move': None, 'right_move': None} for _ in range(0, N + 1)]
    binary_digit_one_list = make_one_count_of_binary_digit(N)
    flag = True
    idx = 1
    count = 1
    while flag:
        if idx == N:
            print(count)
            flag = False
            sys.exit()
        if possibility_list[idx]['left_move'] and possibility_list[idx]['right_move']:
            print(-1)
            flag = False
            sys.exit()
        else:
            possibility_list, idx = move_idx(possibility_list, idx, N)
            count += 1