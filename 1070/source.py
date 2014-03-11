try:
    DP_square = {1: 1}
    DP_rectangle = {}
    while True:
        N = int(raw_input())
        if N == 1:
            print('1 1')
        else:
            S = 0
            for i in range(N, 0, -1):
                if i in DP_square:
                    S += DP_square[i]
                    break
                else:
                    S += pow(i, 2)
            print("{0} {1}".format(S, pow(N + 1, 2)))
except EOFError:
    exit()
