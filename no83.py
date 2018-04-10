if __name__ == '__main__':
    N = int(input())
    q, m = divmod(N, 2)
    if m == 0:
        print(*[1] * q, sep='')
    else:
        q -= 1
        l = [7] + [1] * q
        print(*l, sep='')
