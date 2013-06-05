#!/usr/bin/env python

# This performs a naive sieve that gives an admissible set H that is a factor of 2 from being competitive
from math import *

# The following function was originally by Robert Hanks
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def make_primes(m, n):
    """ Returns  a list of odd primes m <= p < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [i for i in xrange(3,n,2) if sieve[i] and i >= m]

def small_mod(n, p):
    a = n % p
    if a > (p-1)/2:
        return p-a
    return a
def covers(S, p):
    res = [False] * ((p-1)/2)
    for s in S:
        if s != p:
            res[small_mod(s, p)-1] = True
    for i in res:
        if not i:
            return False
    return True

# Find an admissible set with |H| close to 34,429. Competitive value for diam(H) is about 380,000
primes = make_primes(3, 195797)
size = 2*(len(primes)+1)
for p in primes:
    if p > size:
        print "|H| = %s, diam(H) = %s" % (size, 4*primes[-1])
        # |H| = 34478, diam(H) = 783164
        print primes[:100]
        exit()
    if covers(primes, p):
        primes.remove(p)
        size -= 2

# The final set H is constructed from primes as follows:
# let T = {1} u (primes)
# let U = T u -T
# then H = 2U
