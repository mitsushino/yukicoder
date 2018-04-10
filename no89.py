# 参照したURL http://www.suguru.jp/culture/torus.html
import math

if __name__ == '__main__':
    c = int(input())
    r_in, r_out = list(map(int, input().split()))
    r = (r_out - r_in) / 2
    circle = r * r * math.pi
    moved_length = (r + r_in) * 2 * math.pi
    print(c * circle * moved_length)