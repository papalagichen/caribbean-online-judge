from fractions import gcd

N = int(raw_input())
count = 0
for i in range(1, N):
    if gcd(i, N) == 1:
        count += 1
print(count)
