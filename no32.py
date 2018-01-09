# -*- coding: utf-8 -*-

if __name__ == '__main__':
    bill_1000 = 0
    coin_100 = int(input())
    coin_25 = int(input())
    coin_1 = int(input())

    quotient, remainder = divmod(coin_1, 25)
    coin_25 += quotient
    coin_1 = remainder

    quotient, remainder = divmod(coin_25, 4)
    coin_100 += quotient
    coin_25 = remainder

    quotient, remainder = divmod(coin_100, 10)
    bill_1000 += quotient
    coin_100 = remainder

    print(coin_100 + coin_25 + coin_1)
