def make_xor_fib(F0, F1, N):
    xor_fib_list = [F0, F1]
    xor_fib_list.append(int(bin(F0 ^ F1)[2:], 2))
    return xor_fib_list[N % 3]


if __name__ == '__main__':
    input_list = list(map(int, input().split()))
    F0, F1, N = input_list[0], input_list[1], input_list[2]
    print(make_xor_fib(F0, F1, N))
