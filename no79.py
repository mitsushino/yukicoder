from collections import Counter

n = int(input())
l_list = list(map(int, input().split()))
c = Counter(l_list)
l = c.most_common()[0][0]
cnt = c.most_common()[0][1]
for t in c.most_common():
    if t[1] < cnt:
        break
    if t[0] > l:
        l = t[0]
print(l)
