def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n / 3)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = [False] * ((n / 6 - k * k / 6 - 1) / k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = [False] * ((n / 6 - k * (k - 2 * (i & 1) + 4) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n / 3 - correction) if sieve[i]]


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return mid + 1

P = primes2(4567899)

print(binary_search(P, 12))