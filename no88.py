if __name__ == '__main__':
    S = input()
    B = ''
    for _ in range(8):
        B += input()
    if B.count('.') % 2 == 0:
        print(S)
    else:
        if S == 'oda':
            print('yukiko')
        else:
            print('oda')