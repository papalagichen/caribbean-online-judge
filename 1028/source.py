try:
    line = raw_input().strip()
    while line:
        s1, s2 = line.split(' ')
        l1, l2 = len(s1), len(s2)
        i1, i2 = 0, 0
        while i1 < l1 and i2 < l2:
            if s1[i1] == s2[i2]:
                i1 += 1
            i2 += 1
        print('No' if i1 < l1 else 'Yes')
        line = raw_input().strip()
except EOFError:
    exit()
