#!/usr/bin/env python
"""Prepares Hayes' feature charts."""

import collections
import csv
import unicodedata

from typing import Dict, DefaultDict, List

ENGLISH_PATH = "FeaturesForEnglish.csv"
UNIVERSAL_PATH = "Features.csv"


def _process(path: str) -> Dict[str, List[str]]:
    retval: DefaultDict[str, List[str]] = collections.defaultdict(list)
    with open(path, "r") as source:
        reader = csv.DictReader(source)
        for row in reader:
            phone = unicodedata.normalize("NFC", row[""])
            del row[""]
            for name, pole in row.items():
                if pole == "0":
                    continue
                retval[phone].append(pole + name)
    return dict(retval)


def main() -> None:
    print("english = ", end="")
    print(_process(ENGLISH_PATH))
    print()
    print("universal = ", end="")
    print(_process(UNIVERSAL_PATH))


if __name__ == "__main__":
    main()
