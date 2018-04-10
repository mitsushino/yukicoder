import math

if __name__ == '__main__':
    xy = list(map(int, input().split()))
    x, y = xy[0], xy[1]
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    hypotenuse *= 2
    if hypotenuse - int(hypotenuse) == 0:
        print(int(hypotenuse) + 1)
    else:
        print(int(math.ceil(hypotenuse)))
