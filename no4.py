# -*- coding: utf-8 -*-


def make_dp_table(N, sum_weight_list):
    dp = [[False for _ in range(sum_weight_list + 1)] for _ in range(N)]
    for i in range(N):
        if i == 0:
            for j in range(sum_weight_list + 1):
                if j == weight_list[i]:
                    dp[i][j] = True
                    break
        else:
            for j in range(1, sum_weight_list + 1):
                if j == weight_list[i]:
                    dp[i][j] = True
                elif j < weight_list[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - weight_list[i]]
    return dp


if __name__ == '__main__':
    N = int(input())
    weight_list = list(map(int, input().split()))
    weight_list.sort()
    sum_weight_list = sum(weight_list)
    if sum_weight_list % 2 != 0:
        print('impossible')
    else:
        dp = make_dp_table(N, sum_weight_list)
        target_val = int(sum_weight_list / 2)
        if dp[N - 1][target_val]:
            print('possible')
        else:
            print('impossible')
