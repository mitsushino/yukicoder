if __name__ == '__main__':
    N = input()
    N_list = set([int(N)])
    for i in range(len(N) - 1):
        N_tmp = N
        max_index = N_tmp[i:].rfind(max(N_tmp[i:])) + i
        N_tmp = list(N_tmp)
        N_tmp[i], N_tmp[max_index] = N_tmp[max_index], N_tmp[i]
        N_list.add(int(''.join(N_tmp)))
    print(max(N_list))