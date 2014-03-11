line = raw_input()
while int(line):
    s = 0
    for i in range(len(line)):
        d = int(line[i])
        s += d if i % 2 else -d
    print('{0} is {1}a multiple of 11.'.format(line, 'not ' if s % 11 else ''))
    line = raw_input()
