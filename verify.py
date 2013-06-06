#!/usr/bin/env python

# Verification
H = []
for line in open('admissable.txt','r').readlines():
    H.append(int(line))

primes = []
for line in open('primes.txt','r').readlines():
    primes.append(int(line))
    
for p in primes:
    def empty_residue(q):
        for i in xrange(q):
            def has(w):
                for l in H:
                    if l % q == w:
                        return True
                return False
            if not has(i):
                return i
        return None
    a = empty_residue(p)
    if a is None:
        print "Oh no, the prime %s is actually covered!" % p
        exit()
    else:
        print "Admissible mod %s because there is no element %s mod %s" % (p, a, p)

