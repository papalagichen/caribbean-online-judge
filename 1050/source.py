N = int(raw_input())
DP = {}
count = 0
for i in range(1, N):
    a, b = i, N
    while b:
        a, b = b, a % b
        if b in DP:
            a = 1
            break
    if a == 1:
        count += 1
        DP[i] = True
print(count)
