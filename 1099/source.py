line = raw_input()
while line != '0':
    ia = sorted(map(int, line.split(' ')))
    print('right' if pow(ia[0], 2) + pow(ia[1], 2) == pow(ia[2], 2) else 'wrong')
    line = raw_input()
