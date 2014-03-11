FREE = '.'
OBSTACLE = '#'


# return {'start index': 'free length', ...}
def find_square(lines, current_line, index):
    free = {}

    for i in line:
        ''
        pass

    return free


for i in range(int(raw_input())):
    line_count = int(raw_input())
    lines = []
    for i in range(line_count):
        lines.append(raw_input().strip())
    square_size = 0
    for i in len(lines):
        line = lines[i]
        for j in range(len(line), 0, -1):
            if line.index(FREE * j):

    print(square_size)