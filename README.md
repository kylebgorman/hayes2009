Hayes (2009) phonological feature tables
========================================

[![PyPI
version](https://badge.fury.io/py/hayes2009.svg)](https://pypi.org/project/hayes2009)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/hayes2009.svg)](https://pypi.org/project/hayes2009)
[![CircleCI](https://circleci.com/gh/kylebgorman/hayes2009/tree/main.svg?style=svg)](https://circleci.com/gh/kylebgorman/hayes2009/tree/main)

`hayes2009` is a small Python 3.7+ module that exposes phonological feature
tables from the Hayes (2009) phonology textbook.

See [`hayes2009.py`](hayes2009.py) for information about how this data has been
processed.

It exposes two tables: an `english`-only table and a larger `universal` table.
As far as I can tell, phones that occur in English are given the same
specification in both tables but both tables are provided for completeness.

willfix/wontfix
---------------

**Please read before filing an issue on the issue tracker**

I **will** correct the following:

-   Typographical errors in the Hayes' tables

I **will not** accept PRs for any the following:

-   Alternative names for the features
-   "Fancy" (i.e., tuple-based) feature specifications
-   Additional feature specifications from other sources
-   Reverse look-up (i.e., finding phones that match a certain feature
    specification)

Gotchas
-------

-   Hayes uses SHOUTYCASE for the major place features like `LABIAL`.
-   Phones are encoded in
    [NFC](https://en.wikipedia.org/wiki/Unicode_equivalence#Normal_forms).
-   Hayes uses the traditional "single-storey" *ɡ* rather than *g* for the
    voiced velar stop.
-   Hayes includes many contour segments, but these are indicated with the tie
    bars (e.g., *t͡s*).

License
-------

This library is distributed under an Apache 2.0 license. Please see
[`LICENSE.txt`](LICENSE.txt) for detalis.

Author
------

`hayes2009` was written by [Kyle Gorman](kylebgorman@gmail.com).

References
----------

Hayes, B. 2009. *Introductory Phonology*. John Wiley & Sons.

