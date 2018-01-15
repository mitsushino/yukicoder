# -*- coding: utf-8 -*-
# 参考にしたURL
# http://chausson.eng.kagawa-u.ac.jp/Comp/Prog/DosC/Sec4/Note432.html
# http://d.hatena.ne.jp/kazu-yamamoto/20090223/1235372875
# http://ttrsq.exblog.jp/24409121/
M = 1000003


def binary_exponent(x, exponent):
    sum_values = 1
    quotient = exponent
    square_num = x
    while quotient > 0:
        quotient, mod = divmod(quotient, 2)
        if mod == 1:
            sum_values *= square_num
        square_num = pow(square_num, 2) % M
    return sum_values


if __name__ == '__main__':
    xN = list(map(int, input().split()))
    x = xN[0]
    N = xN[1]
    exponent_list = list(map(int, input().split()))
    sum_values = 0
    for exponent in exponent_list:
        sum_values += binary_exponent(x, exponent)
    print(sum_values % M)
