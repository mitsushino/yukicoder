# -*- coding: utf-8 -*-
import math


def make_prime_number_table(N):
    prime_number_table_bool = [True for _ in range(N + 1)]
    prime_number_table_bool[0] = False
    prime_number_table_bool[1] = False
    sqrt = math.sqrt(N)
    i = 2
    while i <= sqrt:
        for j in range(i + 1, N + 1):
            if j % i == 0:
                prime_number_table_bool[j] = False
        i += 1
    prime_number_table = []
    for idx, v in enumerate(prime_number_table_bool):
        if v:
            prime_number_table.append(idx)
    return prime_number_table


if __name__ == '__main__':
    N = int(input())
    prime_number_table = make_prime_number_table(N)
    win_lose_flag_table = [False for i in range(N + 1)]
    win_lose_flag_table[0] = True
    win_lose_flag_table[1] = True
    for i in range(2, N + 1):
        for prime_number in prime_number_table:
            if i < prime_number:
                break
            else:
                if win_lose_flag_table[i - prime_number] == False:
                    win_lose_flag_table[i] = True
                    break
    if win_lose_flag_table[N]:
        print('Win')
    else:
        print('Lose')
