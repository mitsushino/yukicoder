# -*- coding: utf-8 -*-
# 参考URL
# http://blog.livedoor.jp/yoshichi9-solve/archives/16290354.html
from collections import deque


def make_one_count_of_binary_digit(N):
    l = []
    for i in range(0, N + 1):
        l.append(bin(i).count('1'))
    return l


def bfs(N, binary_digit_one_list):
    d = [0 for _ in range(N + 1)]
    d[1] = 1
    q = deque()
    q.append(1)
    while q:
        idx = q.popleft()
        if idx == N:
            return d[idx]
        right = idx + binary_digit_one_list[idx]
        left = idx - binary_digit_one_list[idx]
        if (0 < right <= N) and d[right] == 0:
            q.append(right)
            d[right] = d[idx] + 1
        if (0 < left <= N) and d[left] == 0:
            q.append(left)
            d[left] = d[idx] + 1
    return -1


if __name__ == '__main__':
    N = int(input())
    binary_digit_one_list = make_one_count_of_binary_digit(N)
    print(bfs(N, binary_digit_one_list))
