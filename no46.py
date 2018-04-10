if __name__ == '__main__':
    ab = list(map(int, input().split()))
    a, b = ab[0], ab[1]
    q, mod = divmod(b, a)
    if mod > 0:
        q += 1
    print(q)