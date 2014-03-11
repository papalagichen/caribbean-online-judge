try:
    line = raw_input()
    while line:
        line = line.split(' ')
        print int(line[0]) + int(line[1])
        line = raw_input()
except EOFError:
    exit()