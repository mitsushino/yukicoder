pq = list(map(float, input().split()))
p = pq[0]  # 表向き
rev_p = 1 - p  # 裏向き
q = pq[1]

p1 = rev_p * q
p2 = p * (1 - q) * q
if p1 < p2:
    print('YES')
else:
    print('NO')
