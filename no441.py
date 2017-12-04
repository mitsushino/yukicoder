first, second = map(int, input().split())

s = first + second
p = first * second
if s > p:
    print('S')
elif p > s:
    print('P')
elif s == p:
    print('E')
