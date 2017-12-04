numbers = map(int, input().split())
for i in range(1, 11):
    if i not in numbers:
        print(i)
        break
