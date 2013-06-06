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

Output seems to show that an admissible set is found with diameter **388118**, but it only contains 31475 elements (not 34429):
```
avius@all-in:~/conj$ time ./sutherland.py 
Sifting out 0 mod p for 2 < p < 622
Performing greedy residue removal for 622 <= p <= 34429
[-185662, -185644, -185642, -185632, -185624, -185618, -185608, -185602, -185582, -185578, -185576, -185558, -185552, -185534, -185524, -185522, -185512, -185506, -185488, -185474, -185446, -185434, -185414, -185408, -185404, -185398, -185396, -185386, -185384, -185348, -185342, -185338, -185336, -185314, -185312, -185308, -185294, -185282, -185278, -185272, -185264, -185254, -185246, -185236, -185228, -185204, -185186, -185138, -185134, -185116, -185114, -185102, -185092, -185084, -185056, -185048, -185044, -185014, -185006, -184978, -184958, -184948, -184936, -184934, -184928, -184918, -184916, -184876, -184862, -184838, -184826, -184816, -184802, -184798, -184796, -184792, -184784, -184774, -184768, -184766, -184762, -184754, -184748, -184738, -184732, -184726, -184724, -184714, -184706, -184694, -184684, -184666, -184648, -184634, -184622, -184594, -184588, -184568, -184564, -184538]
[201244, 201284, 201298, 201304, 201328, 201332, 201338, 201346, 201352, 201364, 201368, 201386, 201398, 201406, 201424, 201436, 201452, 201464, 201466, 201482, 201494, 201508, 201512, 201532, 201538, 201548, 201568, 201574, 201598, 201602, 201622, 201632, 201644, 201646, 201658, 201668, 201692, 201694, 201706, 201752, 201764, 201776, 201808, 201814, 201832, 201836, 201862, 201874, 201886, 201896, 201904, 201914, 201944, 201952, 201962, 201974, 201976, 201988, 201998, 202012, 202018, 202024, 202052, 202054, 202088, 202102, 202108, 202126, 202144, 202156, 202172, 202178, 202192, 202196, 202204, 202214, 202222, 202226, 202234, 202238, 202256, 202282, 202298, 202318, 202324, 202336, 202346, 202352, 202364, 202366, 202372, 202394, 202396, 202406, 202408, 202414, 202418, 202424, 202442, 202456]
|H| = 31475, diam(H) = 388118
Admissible mod 631 because there is no element 0 mod 631
Admissible mod 641 because there is no element 0 mod 641
Admissible mod 643 because there is no element 0 mod 643
Admissible mod 1019 because there is no element 0 mod 1019
Admissible mod 2909 because there is no element 405 mod 2909
Admissible mod 5701 because there is no element 1216 mod 5701
Admissible mod 10009 because there is no element 30 mod 10009
Admissible mod 19139 because there is no element 13 mod 19139
Admissible mod 33377 because there is no element 3 mod 33377
Admissible mod 34421 because there is no element 4 mod 34421
Admissible mod 34429 because there is no element 4 mod 34429

real	4m44.211s
user	4m39.420s
sys	0m0.496s
```

See Also
===
[Scott Morrison](https://github.com/semorrison/polymath8)
[Vit Tucek](https://github.com/vit-tucek/admissible_sets)
[Polymath8](http://michaelnielsen.org/polymath1/index.php?title=Bounded_gaps_between_primes)
[Reading seminar](http://terrytao.wordpress.com/2013/06/04/online-reading-seminar-for-zhangs-bounded-gaps-between-primes)
[sbseminar](http://sbseminar.wordpress.com/2013/05/30/i-just-cant-resist-there-are-infinitely-many-pairs-of-primes-at-most-59470640-apart/)

