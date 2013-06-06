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
    for p in make_primes(3, c): # sieve out 0 mod p
        a[(-p) * ((-low)/(2*p)) - low/2::p] = [False] * (high/(2*p) + (-low)/(2*p) + 1)
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

'''
avius@all-in:~/conj$ time python sutherland.py 
[14028, 14031, 14032, 14037, 14043, 14050, 14053, 14056, 14067, 14070, 14071, 14077, 14080, 14082, 14085, 14086, 14095, 14106, 14107, 14113, 14115, 14127, 14131, 14137, 14142, 14148, 14152, 14155, 14157, 14158, 14163, 14172, 14176, 14187, 14191, 14196, 14205, 14206, 14215, 14217, 14220, 14227, 14235, 14241, 14242, 14248, 14250, 14253, 14257, 14263, 14280, 14283, 14292, 14295, 14301, 14302, 14311, 14317, 14320, 14322, 14323, 14326, 14331, 14340, 14346, 14353, 14368, 14371, 14373, 14385, 14386, 14388, 14400, 14406, 14407, 14410, 14413, 14418, 14421, 14422, 14425, 14427, 14430, 14436, 14437, 14446, 14448, 14451, 14457, 14460, 14467, 14473, 14478, 14485, 14487, 14488, 14491, 14493, 14502, 14505]
[199323, 199327, 199333, 199335, 199336, 199342, 199351, 199356, 199357, 199371, 199372, 199377, 199378, 199383, 199398, 199402, 199410, 199411, 199413, 199416, 199417, 199425, 199428, 199437, 199441, 199446, 199452, 199456, 199465, 199482, 199483, 199486, 199488, 199498, 199500, 199507, 199521, 199522, 199533, 199543, 199551, 199558, 199563, 199566, 199567, 199573, 199582, 199585, 199600, 199602, 199615, 199617, 199620, 199623, 199633, 199636, 199645, 199656, 199657, 199663, 199665, 199668, 199672, 199675, 199677, 199678, 199683, 199686, 199696, 199707, 199717, 199720, 199728, 199735, 199738, 199740, 199741, 199743, 199747, 199750, 199752, 199753, 199755, 199761, 199767, 199771, 199776, 199782, 199791, 199798, 199801, 199806, 199810, 199812, 199813, 199815, 199818, 199827, 199830, 199831]
|H| = 34429, diam(H) = 371606

real	4m22.655s
user	4m21.208s
sys	0m0.220s
'''
