import math

if __name__ == '__main__':
    X, Y, L = [int(input()) for _ in range(3)]
    if Y >= 0:
        count = math.ceil(Y / L)
        if X != 0:
            count += 1
            count += math.ceil(abs(X) / L)
    else:
        count = 1
        count += math.ceil(abs(X) / L)
        count += 1
        count += math.ceil(abs(Y) / L)
    print(count)