import sys

if __name__ == '__main__':
    A_list = list(input())
    B = input()
    for s in B:
        if s in A_list:
            A_list.remove(s)
        else:
            print('NO')
            sys.exit()
    print('YES')
