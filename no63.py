if __name__ == '__main__':
    L, K = list(map(int, input().split()))
    K_double = K * 2
    q, mod = divmod(L, K * 2)
    if mod == 0:
        print((q - 1) * K)
    else:
        print(q * K)