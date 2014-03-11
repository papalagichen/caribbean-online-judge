for i in range(int(raw_input())):
    line_count = int(raw_input())
    orders = []
    for n in range(line_count):
        orders.append(map(int, raw_input().strip().split(' ')))
