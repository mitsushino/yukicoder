from collections import Counter

s = input()
c = Counter(s)

p1 = c['0'] * 3 + c['1'] * 2 + c['2'] * 2 + c['3'] * 2 + c['4'] * 3 + c['5'] * 2 + \
     c['6'] * 3 + c['7'] * 2 + c['8'] * 4 + c['9'] * 3 + 1

hole_num = c['0'] + c['4'] + c['6'] + c['8'] * 2 + c['9']
p2 = (1 + hole_num) * 2 + len(s)

print(min(p1, p2))
