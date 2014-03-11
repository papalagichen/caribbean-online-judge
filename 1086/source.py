def primes(n):
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n / 3)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = [False] * ((n / 6 - k * k / 6 - 1) / k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = [False] * (
            (n / 6 - k * (k - 2 * (i & 1) + 4) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n / 3 - correction) if sieve[i]]


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    mid = midval = 0
    while lo < hi:
        mid = (lo + hi) // 2
        midval = a[mid]
        if midval < x:
            lo = mid + 1
        elif midval > x:
            hi = mid
        else:
            return mid + 1
    return mid if x < midval else mid + 1


P = primes(4567899)

try:
    N = int(raw_input())
    while N:
        print(binary_search(P, N))
        N = int(raw_input())
except EOFError:
    exit()
