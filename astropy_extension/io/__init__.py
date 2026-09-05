from typing import Any

import astropy.units as u


def get_units(unit: str | list[Any]) -> Any:
    if isinstance(unit, list):
        return [get_units(v) for v in unit]
    else:
        if unit == "":
            return None
        else:
            v = u.Unit(unit)
            if v.is_equivalent(1):
                return 1 * v
            else:
                return v


def get_values(value: str | list[Any]) -> Any:
    if isinstance(value, list):
        return [get_values(v) for v in value]
    else:
        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            pass

        return value
