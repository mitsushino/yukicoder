# -*- coding: utf-8 -*-

if __name__ == '__main__':
    numbers_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    N = int(input())
    yes_set = set()
    no_set = set()
    for _ in range(N):
        answer_list = input().split()
        if answer_list[4] == 'YES':
            numbers_set = numbers_set & set(answer_list[:4])
        else:
            numbers_set = numbers_set - set(answer_list[:4])
    print(list(numbers_set - no_set)[0])
