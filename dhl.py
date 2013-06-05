#!/usr/bin/env python
import sys
import bitarray
# A set S is admissible if it is not a complete set of residue classes mod anything.

# The following function was written by Robert Hanks
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def make_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [i for i in xrange(3,n,2) if sieve[i]] # don't bother including 2 because nothing covers it
    
def covers_all(H, p):
    residues = [False] * p
    for h in H:
        residues[h % p] = True
    for i in range(p):
        if not residues[i]:
            return False
    return True

def is_admissible(richards, killer, k):
    print killer
    if killer:
        if covers_all(richards, killer):
            print "Witness %s worked again" % killer
            return (False, killer)
            
    for p in primes:
        if killer and p == killer:
            continue
        if covers_all(richards, p):
            print "Witness %s" % p
            return (False, p)
        if p > k:
            return (True, None)
    # exhausted our list of primes
    return True

# Assume k is even.
# richards(m, k) is the set:
# \pm 1, \pm p_{m+1}, \pm p_{m+2}, ..., \pm p_{m-1+k/2}
# with k elements
# \pm primes[m-1], ..., \pm primes[m-3+k/2]
#
# As a speedup, we use the following:
# richards(m+1, k) = richards(m, k) \ { \pm primes[m-1] } U { \pm primes[m-2+k/2] }

k = 10000 #341640 # default for k

if len(sys.argv) > 1:
    k = sys.argv(1)

primes = sorted(make_primes(k), reverse=True) # primes 2 < p < k; primes[i] = p_{l + 1 - i}
l = len(primes)

exit()

# m starts at start + 1
start = 360
end = 365

# For a given k, find a set H subject to:
# |H|=k
# diam(H) is small
# H doesn't cover any p

# the killer prime
killer = None

# build richards(start, k)
richards = set([-1,1])
for i in range(start - 1, start - 2 + k/2):
    richards.add(primes[i])
    richards.add(-primes[i])
for m in range(start, end):
    truth, new_killer = is_admissible(richards, killer, k)
    if truth:
        print "Found m = %s, width = %d" % (m, max(richards) - min(richards))    
        exit()

    killer = new_killer
    # update the richards set
    richards.remove(primes[m-1])
    richards.remove(-primes[m-1])    
    richards.add(primes[m-2+k/2])
    richards.add(-primes[m-2+k/2])

