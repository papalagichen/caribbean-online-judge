total = 0.0
for i in range(12):
    total += float(raw_input())
print('${0:.2f}'.format(total / 12))