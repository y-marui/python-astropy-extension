import tempfile
from pathlib import Path

import astropy.units as u
from astropy.table import QTable

from astropy_extension.io.csv import read_csv

with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=True) as tmpf:
    path = Path(tmpf.name)
    tmpf.write("""A, B, C
a, 1, 1
b, 2, 4
c, 3, 9""")
    tmpf.seek(0)

    assert (read_csv(path) == QTable({"A": ["a", "b", "c"], "B": [1, 2, 3], "C": [1, 4, 9]})).all()

with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=True) as tmpf:
    path = Path(tmpf.name)
    tmpf.write("""A, B, C
 , m, s
a, 1, 1
b, 2, 4
c, 3, 9""")
    tmpf.seek(0)

    assert (read_csv(path, has_unit=True) == QTable({"A": ["a", "b", "c"], "B": [1, 2, 3] * u.m, "C": [1, 4, 9] * u.s})).all()
