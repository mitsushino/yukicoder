# -*- coding: utf-8 -*-


def make_group(card_list):
    card_dic = {}
    mark_set = set()
    number_set = set()
    for card in card_list:
        if card[0] not in card_dic:
            card_dic[card[0]] = set()
        card_dic[card[0]].add(card[1])
        mark_set.add(card[0])
        number_set.add(card[1])
    return card_dic, mark_set, number_set


def calculate_cards(card_dic, mark_set, number_set, W, H):
    count = 0
    for v in card_dic.values():
        count += H - len(v)
    remainder_mark_num = W - len(mark_set)
    count += remainder_mark_num * len(number_set)
    return count


if __name__ == '__main__':
    W = int(input())
    H = int(input())
    N = int(input())
    card_list = [list(map(int, input().split())) for _ in range(N)]
    card_dic, mark_set, number_set = make_group(card_list)
    print(calculate_cards(card_dic, mark_set, number_set, W, H))
