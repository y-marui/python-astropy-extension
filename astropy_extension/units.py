"""Define additional units."""

import astropy.units as u

try:
    sccm: u.Unit = u.Unit("sccm")
except ValueError:
    sccm = u.def_unit("sccm", u.ml / u.m)
    u.add_enabled_units(sccm)

try:
    uohm_cm: u.Unit = u.Unit("uohm_cm")
except ValueError:
    uohm_cm = u.def_unit("uohm_cm", u.uohm * u.cm, format={"latex": r"\mu\Omega\,cm"})
    u.add_enabled_units([uohm_cm])

try:
    A__m2: u.Unit = u.Unit("A__m2")
except ValueError:
    A__m2 = u.def_unit("A__m2", u.A * (u.m**-2), format={"latex": r"A\,m^{-2}"})
    u.add_enabled_units([A__m2])


def get_exponential_as_unit(n):
    try:
        res: u.Unit = u.Unit(f"E{n}")
    except ValueError:
        res: u.Unit = u.def_unit(f"E{{{n}}}", 10**n * u.one, format={"latex": f"10^{{{n}}}"})
        u.add_enabled_units([res])
    return res
