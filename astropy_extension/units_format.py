# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""

from astropy import units as u


class LatexInlineNoFrac(u.format.Latex):
    """
    Output LaTeX to display the unit based on IAU style guidelines with negative
    powers.

    Attempts to follow the `IAU Style Manual
    <https://www.iau.org/static/publications/stylemanual1989.pdf>`_ and the
    `ApJ and AJ style guide
    <https://journals.aas.org/manuscript-preparation/>`_.
    """

    name = "latex_inline_no_flac"

    @classmethod
    def to_string(cls, unit, fraction="inline"):
        return super().to_string(unit, fraction=fraction)
