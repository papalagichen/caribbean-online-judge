T = int(raw_input())
for i in range(T):
    raw_input()
    N = int(raw_input())
    candies = 0
    for j in range(N):
        candies += int(raw_input())
    print('NO' if candies % N else 'YES')
