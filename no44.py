if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if i + 1 <= N:
            dp[i + 1] += dp[i]
        if i + 2 <= N:
            dp[i + 2] += dp[i]
    print(dp[N])
