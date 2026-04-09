# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""

import astropy.units as u
import numpy as np
import numpy.ma as ma


def labeled_quantity_support(xlabel="", ylabel="", format=u.format.LatexInline):
    """Excute quantity_support with label.

    Enable support for plotting `astropy.units.Quantity` instances i
    n matplotlib.
    May be (optionally) used with a ``with`` statement.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from astropy import units as u
    >>> from astropy import visualization
    >>> with visualization.quantity_support():
    ...     plt.figure()
    ...     plt.plot([1, 2, 3] * u.m)
    [...]
    ...     plt.plot([101, 125, 150] * u.cm)
    [...]
    ...     plt.draw()

    Parameters
    ----------
    format: `astropy.units.format.Base` instance or str
        The name of a format or a formatter object.  If not
        provided, defaults to ``latex_inline``.

    """
    import matplotlib as mtlb
    from astropy import units as u
    from matplotlib import ticker, units

    def rad_fn(x, pos=None):
        n = int((x / np.pi) * 2.0 + 0.25)
        if n == 0:
            return "0"
        elif n == 1:
            return "π/2"
        elif n == 2:
            return "π"
        elif n % 2 == 0:
            return "{}π".format(n / 2)
        else:
            return "{}π/2".format(n)

    class MplQuantityConverter(units.ConversionInterface):
        def __init__(self):
            if u.Quantity not in units.registry:
                units.registry[u.Quantity] = self
                self._remove = True
            else:
                self._remove = False

        @staticmethod
        def axisinfo(unit, axis):
            if isinstance(axis, mtlb.axis.XAxis):
                axis_label = xlabel
            elif isinstance(axis, mtlb.axis.YAxis):
                axis_label = ylabel
            else:
                axis_label = ""

            if unit in [None, u.dimensionless_unscaled, u.dimensionless_angles]:
                label = axis_label
            else:
                label = "{} ({})".format(axis_label, unit.to_string(format))

            # if unit == u.radian:
            #     return units.AxisInfo(
            #         majloc=ticker.MultipleLocator(base=np.pi/2),
            #         majfmt=ticker.FuncFormatter(rad_fn),
            #         label=label,
            #     )
            # el
            if unit == u.degree:
                return units.AxisInfo(
                    majloc=ticker.AutoLocator(),
                    majfmt=ticker.FormatStrFormatter("%i°"),
                    label=label,
                )
            elif unit is not None:
                return units.AxisInfo(label=label)
            return None

        @staticmethod
        def convert(val, unit, axis):
            if isinstance(val, u.Quantity):
                return val.to_value(unit)
            elif isinstance(val, ma.masked_array) and isinstance(val.data, u.Quantity):
                return val.data.to_value(unit)
            elif isinstance(val, list) and isinstance(val[0], u.Quantity):
                return [v.to_value(unit) for v in val]
            else:
                return val

        @staticmethod
        def default_units(x, axis):
            if hasattr(x, "unit"):
                return x.unit
            elif isinstance(x, ma.masked_array) and hasattr(x.data, "unit"):
                return x.data.unit
            return None

        def __enter__(self):
            return self

        def __exit__(self, type, value, tb):
            if self._remove:
                del units.registry[u.Quantity]

    return MplQuantityConverter()
