count = int(raw_input())
for i in range(count):
    a, b = map(int, raw_input().split(' '))
    sum = 0
    for i in xrange(a, b + 1):
        sum += i * (i + 1) * (i + 2)
    print(sum % 100)
