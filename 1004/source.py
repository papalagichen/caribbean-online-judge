for i in range(int(raw_input())):
    N, M = map(int, raw_input().strip().split(' '))
    if N > M:
        if M % 2 == 0:
            print('U')
        else:
            print('D')
    elif N < M:
        if N % 2 == 0:
            print('L')
        else:
            print('R')
    else:
        if N % 2 == 0:
            print('L')
        else:
            print('R')