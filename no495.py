s = input()
left = s.count('(^^*)')
right = s.count('(*^^)')
print('{} {}'.format(left,right))