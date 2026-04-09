import csv
from pathlib import Path

from astropy.table import QTable

from . import get_units, get_values


def read_csv(path: Path, has_unit: bool = False, remove_sharp: bool = False) -> QTable:
    if remove_sharp:
        _table = read_csv(path, has_unit=has_unit)
        _colnames = [c for c in _table.colnames if not c.startswith("#")]
        return _table[_colnames]
    else:
        with path.open("r") as fp:
            reader = csv.reader(fp, skipinitialspace=True)
            _data = [row for row in reader]

        if has_unit:
            _dataset = get_values(_data[2:])
            _colnames = _data[0]
            _units = _data[1]
            return QTable(dict(zip(_colnames, list(zip(*_dataset)))), units=get_units(_units))

        else:
            _dataset = get_values(_data[1:])
            _colnames = _data[0]
            return QTable(dict(zip(_colnames, list(zip(*_dataset)))))
