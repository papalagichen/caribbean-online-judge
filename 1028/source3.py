try:
    line = raw_input().strip()
    while line:
        s1, s2 = map(list, line.split(' '))
        i1, i2 = 0, 0
        for i1 in range(len(s1)):
            c1 = s1[i1]
            while i2 < len(s2):
                c2 = s2[i2]
                i2 += 1
                if c1 == c2:
                    break
            if i2 >= len(s2):
                break
        if i1 + 1 >= len(s1):
            print('Yes')
        else:
            print('No')
        line = raw_input().strip()
except EOFError:
    exit()
