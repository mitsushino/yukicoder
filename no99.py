n = int(input())
l = list(map(int, input().split()))
even_odd_list = [0 if i % 2 == 0 else 1 for i in l]
print(abs(even_odd_list.count(0) - even_odd_list.count(1)))
