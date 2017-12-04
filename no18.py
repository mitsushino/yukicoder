# -*- coding: utf-8 -*-
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def usa_code(idx, c):
    alphabet_idx = alphabet.index(c)
    while idx > 0:
        alphabet_idx -= 1
        if alphabet_idx < 0:
            alphabet_idx = len(alphabet) - 1
        idx -= 1
    return alphabet[alphabet_idx]


if __name__ == '__main__':
    input_str = input()
    joint_str = ''
    for idx, c in enumerate(input_str, 1):
        joint_str += usa_code(idx, c)
    print(joint_str)
