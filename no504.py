people_num = int(input())
k_score = int(input())
current_rank = 1
print(1)
for _ in range(1, people_num):
    if int(input()) > k_score:
        current_rank += 1
        print(current_rank)
    else:
        print(current_rank)