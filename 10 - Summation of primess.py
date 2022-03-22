import math
 
limit = 2* 10**6
highest_factor = int(math.floor(math.sqrt(limit)))
is_prime = [False] * limit
# i, j and n will be dynamically created
for i in xrange(1, highest_factor):
    for j in xrange(1, highest_factor):
        n = 4*i**2+j**2
        if n <= limit and ((n % 12 == 1) or (n % 12 == 5)):
            is_prime[n] = not is_prime[n]
            n = 3*i**2+j**2
        if n <= limit and (n % 12 == 7):
            is_prime[n] = not is_prime[n]
            n = 3*i**2 - j**2
        if n <= limit and (i > j) and (n % 12 == 11):
            is_prime[n] = not is_prime[n]

for i in xrange(5, highest_factor):
    if is_prime[i]:
        for j in xrange(i**2, limit, i**2):
            is_prime[j] = False
 
sumsum = 5
for i in xrange(5, limit):
    if is_prime[i]:
        sumsum = sumsum + i
            
print sumsum