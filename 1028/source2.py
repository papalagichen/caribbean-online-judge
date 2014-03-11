import re


try:
    line = raw_input().strip()
    while line:
        s1, s2 = line.split(' ')
        pattern = ".*".join(s1)
        if re.search(pattern, s2):
            print('Yes')
        else:
            print('No')
        line = raw_input().strip()
        pass
except EOFError:
    exit()