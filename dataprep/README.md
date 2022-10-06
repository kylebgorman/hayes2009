To regenerate the table, simply:

* Manually remove the existing tables from
  [`../hayes2009.py`](../hayes2009.py).
* Run the following:

      ./prepare.py >> ../hayes2009.py
      black -l79 ../hayes2009.py

* Then add, commit, and push changes if necessary.
