# -*- coding: utf-8 -*-
def decide_win_or_lose(N, K):
    if N <= K:
        print('Win')
        return
    N -= 1
    while N > 0:
        N -= (K + 1) # N % (K + 1) == 0のほうが速い？
    if N == 0:
        print('Lose')
    else:
        print('Win')


if __name__ == '__main__':
    P = int(input())
    pair_number_list = [list(map(int, input().split())) for _ in range(P)]
    for pair_number in pair_number_list:
        N = pair_number[0]
        K = pair_number[1]
        decide_win_or_lose(N, K)
