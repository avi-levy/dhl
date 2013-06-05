#!/usr/bin/env python
import sys
import math
from collections import defaultdict
# A set S is admissible if it is not a complete set of residue classes mod anything.

# Assume k is even.
# richards(m, k) is the set:
# \pm 1, \pm p_{m+1}, \pm p_{m+2}, ..., \pm p_{m-1+k/2}

def make_richards(m):
    global k
    richards = set([-1,1])
    for i in range(1, k/2):
        richards.add(natural_primes[m + i - 2]) # p_{m+i}
        richards.add(-natural_primes[m + i - 2])
    return richards
    
def update(richards):
    global k
    richards.remove(natural_primes[last_remove])
    richards.remove(-natural_primes[last_remove])    
    richards.add(natural_primes[last_remove+k/2])
    richards.add(-natural_primes[last_remove+k/2])

# The following function was written by Robert Hanks
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def make_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [i for i in xrange(3,n,2) if sieve[i]] # we don't need 2
    
def covers_all(H, p): # kind of memoized
    global last_witness
    global last_set
    if (not last_witness) or (not last_set) or (last_witness is not p):
        last_set = defaultdict(set)
        for h in H:
            last_set[h % p].add(h)
        for v in last_set.itervalues():
            if not v:
                last_witness = None
                return False
        return True
    else:
        temp = natural_primes[last_remove]
        a = temp % p
        last_set[a].remove(temp)
        temp = -natural_primes[last_remove]      
        b = temp % p          
        last_set[b].remove(temp)        
        temp = natural_primes[last_remove+k/2]
        last_set[temp % p].add(temp)
        temp = -natural_primes[last_remove+k/2]        
        last_set[temp % p].add(temp)
        if last_set[a] and last_set[b]:
            return True
        last_witness = None
        return False                

def is_admissible(richards):
    global k
    for p in primes:
        if covers_all(richards, p):
            print "Witness %s" % p
            return False
    return True


k = 10000 #341640 # default for k

# bounds on m
start = 360
end = 385

if len(sys.argv) > 1:
    k = sys.argv(1)

primes = sorted(make_primes(k), reverse=True) # primes 2 < p < k
l = len(primes) # primes[i] = p_{l + 1 - i}

natural_primes = make_primes(int(math.log(k)*k)) # primes 2 < p, natural_primes[i] = p_{i+2}

# For a given k, find a set H subject to:
# |H|=k
# diam(H) is small
# H doesn't cover any p

last_witness = None
last_set = None
last_remove = None

richards = make_richards(start)
for m in range(start, end):
    if is_admissible(richards):
        print "Found m = %s, width = %d" % (m, max(richards) - min(richards))    
        exit()

    # update the richards set
    # richards(m+1, k) = richards(m, k) \ { \pm p_{m + 1} } U { \pm p_{m + k/2 + 1} }
    
    last_remove = m-1
    update(richards)

