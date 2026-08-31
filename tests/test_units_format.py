import astropy.units as u

from astropy_extension.units_format import LatexInlineNoFrac


def test_name():
    assert LatexInlineNoFrac.name == "latex_inline_no_flac"


def test_to_string_defaults_to_inline_fraction():
    result = LatexInlineNoFrac.to_string(u.m / u.s)
    expected = u.format.Latex.to_string(u.m / u.s, fraction="inline")
    assert result == expected


def test_to_string_via_unit_format_registry():
    # Custom formats are looked up by `name`; astropy's dispatch passes extra
    # kwargs (e.g. `deprecations`) that must be forwarded, not just `fraction`.
    result = (u.m / u.s).to_string(format="latex_inline_no_flac")
    assert result == LatexInlineNoFrac.to_string(u.m / u.s)


def test_to_string_honors_fraction_override():
    result = LatexInlineNoFrac.to_string(u.m / u.s, fraction=False)
    expected = u.format.Latex.to_string(u.m / u.s, fraction=False)
    assert result == expected
