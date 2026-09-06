# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""

from typing import Any

from astropy import units as u


class LatexInlineNoFrac(u.format.Latex):  # type: ignore[misc]
    """
    Output LaTeX to display the unit based on IAU style guidelines with negative
    powers.

    Attempts to follow the `IAU Style Manual
    <https://www.iau.org/static/publications/stylemanual1989.pdf>`_ and the
    `ApJ and AJ style guide
    <https://journals.aas.org/manuscript-preparation/>`_.
    """

    # astropy ships no inline type stubs for `units.format.Latex`, so mypy
    # sees it as `Any` and flags the subclass; see issue #34.
    name = "latex_inline_no_flac"

    @classmethod
    def to_string(
        cls, unit: u.UnitBase, fraction: bool | str = "inline", **kwargs: Any
    ) -> str:
        # `Latex.to_string` is untyped (see the class-level note above), so
        # mypy infers its return as `Any` here.
        return super().to_string(unit, fraction=fraction, **kwargs)  # type: ignore[no-any-return]
