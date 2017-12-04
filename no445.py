from math import floor

star_num, solve_num = map(int, input().split())

score = 50 * star_num + 50 * star_num / (0.8 + 0.2 * solve_num)
print(floor(score))
