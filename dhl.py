#!/usr/bin/env python
import sys
# A set s is admissible if it doesn't cover all the residue classes mod p for all primes p
def is_admissible(H):
    l = len(H)
    for p in primes:
        if p >= l:
            return True
        if covers_all(H, p):
            return False
    # if we get here, we exhausted our list of primes and the result is meaningless
    return True
def covers_all(H, p):
    residues = set(range(p))
    for h in H:
        residues.discard(h % p)
        if not residues:
            return True
    return False
def richards(m, k):
    ret = set([-1,1])
    for i in range(m, m + (k+1)/2):
        ret.add(primes[i])
        ret.add(-primes[i])
    return ret

primes = [int(line) for line in open('primes', 'r').readlines()] # assuming you have a large list of primes in a text file called primes
k = 341640 # default for k
if len(sys.argv) > 1:
    k = sys.argv(1)
M = 6000 # cutoff for m
for m in range(1, M):
    cur = richards(m, k)
    if is_admissible(cur):
        print "Found m = %s, width = %d" % (m, max(cur) - min(cur))
