# -*- coding: utf-8 -*-
# 参考にしたURL
# http://cocodrips.hateblo.jp/entry/2014/02/02/011119
# https://endoyuta.com/2017/02/07/python3-%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3/
import math


def prime_factorization(N):
    i = 2
    count = 0
    while i <= math.sqrt(N):
        if N % i == 0:
            N //= i
            count += 1
            if count > 2:
                print('YES')
                return
        else:
            i += 1
    if N > 1:
        count += 1
        if count > 2:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    N = int(input())
    prime_factorization(N)