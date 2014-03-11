try:
    h1, m1, h2, m2 = map(int, raw_input().split(' '))
    while h1 + m1 + h2 + m2 > 0:
        s1 = h1 * 60 + m1
        s2 = h2 * 60 + m2
        if s2 < s1:
            s2 += 60 * 24
        print(s2 - s1)
        h1, m1, h2, m2 = map(int, raw_input().split(' '))
except:
    exit()
