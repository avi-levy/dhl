dhl
===

Admissible sets for the Dickson-Hardy-Littlewood Conjecture

Overview
===

* `sutherland.py` implements [Andrew Sutherland's algorithm](http://sbseminar.wordpress.com/2013/05/30/i-just-cant-resist-there-are-infinitely-many-pairs-of-primes-at-most-59470640-apart/#comment-23566) to sift intervals until they are admissible. The results are written to `admissible-py.txt` and verified by `verify.py`

* `verify.py` verifies that a set is admissible

* `genprime.py` generates primes and writes them to `primes.txt`

* `dhl.py` does *NOT* work properly in its current form, but it was meant to generate symmetric Richards-Henley sequences

Results
===

`sutherland.py` currently sifts the interval `[-185662, 202456]` to create an admissible set with 34429 elements and diameter 388118, which yields the current world record on bounded gaps between primes.

See Also
===

* [Scott Morrison](https://github.com/semorrison/polymath8)

* [Vit Tucek](https://github.com/vit-tucek/admissible_sets)

* [Polymath8](http://michaelnielsen.org/polymath1/index.php?title=Bounded_gaps_between_primes)

* [Reading seminar](http://terrytao.wordpress.com/2013/06/04/online-reading-seminar-for-zhangs-bounded-gaps-between-primes)

* [sbseminar](http://sbseminar.wordpress.com/2013/06/05/more-narrow-admissible-sets/)

