# -*- coding: utf-8 -*-

if __name__ == '__main__':
    cup = int(input())
    shuffle_time = int(input())
    for _ in range(shuffle_time):
        exchange = list(map(int, input().split()))
        exchange1 = exchange[0]
        exchange2 = exchange[1]
        if exchange1 == cup:
            cup = exchange2
        elif exchange2 == cup:
            cup = exchange1
    print(cup)
