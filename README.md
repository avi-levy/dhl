dhl
===

Admissible sets for the Dickson-Hardy-Littlewood Conjecture

Overview
===

* `sutherland.py` implements [Andrew Sutherland's algorithm](http://sbseminar.wordpress.com/2013/05/30/i-just-cant-resist-there-are-infinitely-many-pairs-of-primes-at-most-59470640-apart/#comment-23566) to sift intervals until they are admissible
* `naive-sieve.py` sifts an interval in a completely symmetric fashion, and generates non-competitive results (the sets are about a factor of 2 not dense enough it seems)
* `dhl.py` does *NOT* work properly in its current form, but it was meant to generate symmetric Richards-Henley sequences

Results
===

`sutherland.py` currently uses parameters sieve(-185662, 202456, 34429), which means it sieves the interval `[-185662, 202456]` looking for an admissible set with 34429 elements.

Output seems to show that an admissible set is found with diameter only **357032**:
```
avius@all-in:~/conj$ time python sutherland.py 
[-154576, -154558, -154556, -154552, -154538, -154534, -154526, -154522, -154516, -154498, -154486, -154478, -154474, -154472, -154444, -154436, -154426, -154412, -154408, -154402, -154384, -154382, -154372, -154342, -154334, -154312, -154306, -154304, -154288, -154282, -154276, -154274, -154268, -154244, -154228, -154202, -154186, -154184, -154172, -154162, -154144, -154138, -154136, -154096, -154094, -154082, -154072, -154064, -154058, -154046, -154034, -154016, -154006, -154004, -153992, -153982, -153968, -153926, -153922, -153904, -153898, -153896, -153886, -153848, -153844, -153838, -153836, -153826, -153814, -153812, -153808, -153796, -153788, -153752, -153746, -153742, -153728, -153724, -153704, -153694, -153688, -153674, -153662, -153658, -153656, -153638, -153632, -153616, -153602, -153572, -153568, -153562, -153554, -153542, -153536, -153514, -153508, -153506, -153484, -153466]
[201398, 201406, 201424, 201436, 201452, 201464, 201466, 201472, 201482, 201494, 201508, 201512, 201532, 201538, 201548, 201568, 201574, 201598, 201602, 201616, 201622, 201632, 201644, 201646, 201658, 201668, 201692, 201694, 201706, 201752, 201764, 201776, 201808, 201814, 201826, 201832, 201836, 201844, 201854, 201862, 201874, 201886, 201896, 201904, 201914, 201944, 201952, 201962, 201974, 201976, 201988, 201998, 202012, 202018, 202024, 202042, 202052, 202054, 202088, 202102, 202108, 202112, 202126, 202144, 202156, 202162, 202172, 202178, 202192, 202196, 202204, 202214, 202222, 202226, 202234, 202238, 202256, 202282, 202298, 202318, 202322, 202324, 202336, 202346, 202348, 202352, 202364, 202366, 202372, 202394, 202396, 202406, 202408, 202414, 202418, 202424, 202432, 202442, 202448, 202456]
|H| = 34429, diam(H) = 357032

real	4m14.606s
user	4m10.800s
sys	0m0.328s
```
