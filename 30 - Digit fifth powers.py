numsum = 0
for n in range(2,1000000):
    nstr = str(n)
    subsum = 0
    for char in nstr:
        subsum = subsum + int(char)**5
    if subsum == n:
        numsum = numsum + n
        print n, numsum
        