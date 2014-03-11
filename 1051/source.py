N = int(raw_input())
M = N % 3
print(N / 3 * 2 + (M - 1 if M else 0))