# -*- coding: utf-8 -*-
# 参考URL
# http://twilog.org/meguru_comp/search?word=%E3%80%90yukicoder%20No.22%E3%80%91&ao=a

def search_symmetry_brackets(K):
    bracket_list = list(input())
    bracket_list_num = []
    for idx, s in enumerate(bracket_list, 1):
        bracket_list_num.append(idx)
        if s == ')':
            idx1 = bracket_list_num.pop()
            idx2 = bracket_list_num.pop()
            if idx1 == K:
                return idx2
            if idx2 == K:
                return idx1


if __name__ == '__main__':
    NK = list(map(int, input().split()))
    N, K = NK[0], NK[1]
    print(search_symmetry_brackets(K))
