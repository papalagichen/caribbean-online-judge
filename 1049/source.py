try:
    raw = raw_input()
    while raw:
        N = int(raw)
        N += 1 if N > 0 else -1
        print(reduce(lambda x, y: x + y, xrange(0, N, 1 if N > 0 else -1)) + (0 if N > 0 else 1))
        raw = raw_input()
except EOFError:
    exit()
