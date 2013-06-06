#!/usr/bin/env python

# Sutherland's algorithm for dense admissible sets, in python
# http://sbseminar.wordpress.com/2013/05/30/i-just-cant-resist-there-are-infinitely-many-pairs-of-primes-at-most-59470640-apart/#comment-23566
from math import *
from collections import defaultdict

# The following function was originally by Robert Hanks
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def make_primes(m, n):
    """ Returns  a list of odd primes m <= p < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [i for i in xrange(3,n,2) if sieve[i] and i >= m]

def sieve(low, high, k): # sieve the interval [low, high] to make it admissible
    B = high - low # assume low, high are both even
    r = xrange(1 + B/2) # choose coordinates that automatically sift out 1 mod 2
    a = [True] * (1 + B/2) # a[i] is a boolean signifying whether (low + 2i) is in the sifted set
    c = int(sqrt(B))
    print "Sieving out 0 mod p for 2 < p < %s" % c
    for p in make_primes(3, c): # sieve out 0 mod p
        a[(-p) * ((-low)/(2*p)) - low/2::p] = [False] * (high/(2*p) + (-low)/(2*p) + 1)
    print "Performing greedy residue removal for %s <= p <= %s" % (c, k)
    for p in make_primes(c, k+1):
        d = defaultdict(int)
        for i in r:
            if a[i]:
                d[i % p] += 1
        m = None
        for i in xrange(p): # compute the residue class, j, with fewest elements
            if not m or d[i] < m:
                j = i
                m = d[i]
        if m > 0: # sift out the class j, if necessary
            for i in r:
                if a[i] and i % p is j:
                    a[i] = False
    return [low + 2*i for i in r if a[i]][-k:] # last k elements of sifted set
out = sieve(-185662, 202456, 34429)
print out[:100]
print out[-100:]
print "|H| = %s, diam(H) = %s" % (len(out), out[-1] - out[0])
