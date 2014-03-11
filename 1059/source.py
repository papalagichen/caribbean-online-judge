N = int(raw_input())
while N:
    binary = '{0:b}'.format(N)
    print('The parity of {0} is {1} (mod 2).'.format(binary, binary.count('1')))
    N = int(raw_input())
