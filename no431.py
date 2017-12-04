f = list(map(int, input().split()))

if f[-1] or sum(f[:3]) < 2:
    print('SURVIVED')
else:
    print('DEAD')
