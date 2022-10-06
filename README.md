hayes2009
=========

`hayes2009` is a small Python 3.7+ module that exposes phonological features
from:

Hayes, B. 2009. Introductory Phonology. John Wiley & Sons.

See [`hayes2009.py`](hayes2009.py) for information about how this data has been
processed.

It exposes two tables: an `english`-only table and a larger `universal` table.
As far as I can tell, phones that occur in English are given the same
specification in both tables but both tables are provided for completeness.

willfix/wontfix
---------------

**Please read before filing an issue on the issue tracker**

I **will** correct the following bugs:

-   Typographical errors in the Hayes' tables

I **will not** work on or accept PRs for any the following "feature requests":

-   Additional feature specifications from other sources
-   Alternative names for the features
-   "Fancy" (i.e., tuple-based) feature specifications
-   Reverse look-up (i.e., finding phones that match a certain feature
    specification)

Gotchas
-------

-   Phones are encoded in
    [NFC](https://en.wikipedia.org/wiki/Unicode_equivalence#Normal_forms).
-   Hayes uses the traditional "single-storey" *ɡ* rather than *g* for the
    voiced velar stop.
-   Hayes includes many contour segments, but these are indicated with the tie
    bars (e.g., *t͡s*).
-   Hayes uses SHOUTYCASE for the major place features like `LABIAL`.

License
-------

This library is distributed under an Apache 2.0 license. Please see
[`LICENSE.txt`](LICENSE.txt) for detalis.

Author
------

`hayes2009` was written by [Kyle Gorman](kylebgorman@gmail.com).
