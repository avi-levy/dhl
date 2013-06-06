#!/usr/bin/env python

# Sutherland's algorithm for dense admissible sets, in python
# http://sbseminar.wordpress.com/2013/05/30/i-just-cant-resist-there-are-infinitely-many-pairs-of-primes-at-most-59470640-apart/#comment-23566
from math import *
from collections import defaultdict

# The following function was originally by Robert Hanks
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def make_primes(m, n):
    """ A = {2 < p < m}, B = {m <= p < n} """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    A = []
    B = []
    for i in xrange(3,n,2):
        if sieve[i]:
            if i < m:
                A.append(i)
            else:
                B.append(i)
    return (A, B)

def sieve(low, high, k): # sieve the interval [low, high] to make it admissible
    B = high - low # assume low, high are both even
    r = xrange(1 + B/2) # choose coordinates that automatically sift out 1 mod 2
    a = [True] * (1 + B/2) # a[i] is a boolean signifying whether (low + 2i) is in the sifted set
    c = int(sqrt(B))
    small, midsize = make_primes(c, k+1)
    print "Sifting out 0 mod p for 2 < p < %s" % c
    for p in small: # sieve out 0 mod p
        a[(-p) * ((-low)/(2*p)) - low/2::p] = [False] * (high/(2*p) + (-low)/(2*p) + 1)
    print "Performing greedy residue removal for %s <= p <= %s" % (c, k)
    for p in midsize:
        d = defaultdict(int)
        for i in r:
            if a[i]:
                d[(low + 2*i) % p] += 1
#        print d
        m = None
        for i in xrange(p): # compute the residue class, j, with fewest elements
            if not m or d[i] < m:
                j = i
                m = d[i]
        if m > 0: # sift out the class j, if necessary
#            print "sifting out %s mod %s (%s elements)" % (j, p, m)
            for i in r:
                if a[i] and ((low + 2*i) % p == j):
#                    print "removing %s" % (low + 2*i)
                    a[i] = False
    return [low + 2*i for i in r if a[i]][-k:] # last k elements of sifted set

out = sieve(-185662, 202456, 34429)

# show part of the head/tail of the list
print out[:100]
print out[-100:]

print "|H| = %s, diam(H) = %s" % (len(out), out[-1] - out[0])

# seat-of-the-pants verification
small_primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,607,613,617,619]
midsize_primes = [631, 641, 643, 1019, 2909, 5701, 10009, 19139, 33377, 34421, 34429]
for i in out:
    if i in small_primes:
        print "Oh no, actually had %s" % i
for p in midsize_primes:
    def empty_residue(q):
        for i in xrange(q):
            def has(w):
                for l in out:
                    if l % q == w:
#                        print "has %s = %s mod %s" % (l, w, q)
                        return True
                return False
            if not has(i):
                return i
        return None
    a = empty_residue(p)
    if a is None:
        print "Oh no, the prime %s is actually covered!" % p
    else:
        print "Admissible mod %s because there is no element %s mod %s" % (p, a, p)
