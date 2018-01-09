# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    N = int(input())
    count = 0
    while N > 1:
        N = math.ceil(N / 2)
        count += 1
    print(count)
