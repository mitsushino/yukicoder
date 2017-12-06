# -*- coding: utf-8 -*-
# todo:他の回答を確認する

def search_symmetry_brackets(idx, bracket_list, bracket):
    if bracket == '(':
        for i in range(idx, -1, -1):
            if bracket_list[i] == '(':
                bracket_list[idx] = ''
                bracket_list[i] = ''
                return i
    else:
        for i in range(idx, len(bracket_list)):
            if bracket_list[i] == ')':
                bracket_list[idx] = ''
                bracket_list[i] = ''
                return i


if __name__ == '__main__':
    NK = list(map(int, input().split()))
    N, K = NK[0], NK[1]
    K -= 1
    bracket_list = list(input())
    search_bracket = bracket_list[K]
    f = True
    idx = K
    if search_bracket == '(':
        while f:
            if bracket_list[idx] == ')':
                symmetry_bracket_idx = search_symmetry_brackets(idx, bracket_list, search_bracket)
                if symmetry_bracket_idx == K:
                    print(idx + 1)
                    f = False
                else:
                    idx = K
            else:
                idx += 1
    else:
        while f:
            if bracket_list[idx] == '(':
                symmetry_bracket_idx = search_symmetry_brackets(idx, bracket_list, search_bracket)
                if symmetry_bracket_idx == K:
                    print(idx + 1)
                    f = False
                else:
                    idx = K
            else:
                idx -= 1
