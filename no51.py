# -*- coding: utf-8 -*-

if __name__ == '__main__':
    W = int(input())
    D = int(input())

    for i in range(D, 0, -1):
        workload = W // pow(i, 2)
        if i == 1:
            print(workload)
        W -= workload
