#!/usr/bin/env python

# Sutherland's algorithm for dense admissible sets, in python
# http://sbseminar.wordpress.com/2013/05/30/i-just-cant-resist-there-are-infinitely-many-pairs-of-primes-at-most-59470640-apart/#comment-23566
from math import *
from collections import defaultdict

def construct(a, b, cutoff):
    print "Sifting out small odd primes" # construct the set [+- 2^n * p] ^ [-a, b] where p is 1 or a prime > cutoff
    sift = []
    def sift_build(end, sign):
        r = range(1,int(log(end,2)/2))    
        for p in primes:
            if p <= cutoff:
                continue
            if p > end:
                break
            for j in r:
                q = p * 2**j
                if q > end:
                    break
                sift.append(q if sign else -q)
    sift_build(a, False)
    sift.extend([-2**j for j in range(1,int(log(a,2))+1)])
    sift.extend([ 2**j for j in range(1,int(log(b,2))+1)])
    sift_build(b, True)
    return sift

def sieve(a, b, k): # Sieve the interval [a, b] to make it admissible
    a = -a
    if not (a > 0 and b > a): # assume 0 < a < b
        exit("Bad bounds, expected [-M, N]")
    cutoff = int(sqrt(b))
    sifted = construct(a, b, cutoff)
    num_left = len(sifted)
    indices = range(num_left) # for efficiency, never actually remove elements from the sift; just set them to 0
    if num_left <= k:
        print "The sieve was too restrictive; only %s elements remained." % num_left
        exit()
    else:
        print "After the 0 mod p sieve, %s elements remain" % num_left

    print "Performing greedy residue removal for %s < p <= %s" % (cutoff, k)
    for p in primes:
        if p <= cutoff:
            continue
        if p > k:
            break;
        d = defaultdict(int)
        for i in indices:
            if sifted[i]: # 0 is used as a sentinel for deleted entries
                d[sifted[i] % p] += 1
        m = None
        for i in range(p): # compute the residue class, j, with fewest elements
            if d[i] == 0:
                j = i
                m = 0
                break
            if not m or d[i] < m:
                j = i
                m = d[i]
        if m > 0: # sift out the class j, if necessary
            for i in indices:
                if sifted[i] and (sifted[i] % p == j):
                    sifted[i] = 0
    return [i for i in sifted if i][:k] # last k elements of sifted set

primes = [] # odd primes <= 200000
for line in open('primes.txt','r').readlines():
    primes.append(int(line))
    
admissible = sieve(-185662, 202456, 34429)

print "|H| = %s, diam(H) = %s" % (len(admissible), max(admissible)-min(admissible))

f = open('admissible-py.txt','w')
for h in sorted(admissible):
  f.write("%s\n" % h)
f.close()
