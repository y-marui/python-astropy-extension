import astropy.units as u

from astropy_extension.io import get_units

assert get_units(["", "m", "s"]) == [None, u.m, u.s]
