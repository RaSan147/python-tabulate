"""API properties.

"""

from tabulate2 import tabulate, tabulate_formats, simple_separated_format
from common import skip


try:
    from inspect import signature, _empty
except ImportError:
    signature = None
    _empty = None


def test_tabulate_formats():
    "API: tabulate_formats is a list of strings"
    supported = tabulate_formats
    assert type(supported) is list
    for fmt in supported:
        assert type(fmt) is str  # noqa


def _check_signature(function, expected_sig):
    if not signature:
        skip("")
    actual_sig = signature(function)
    actual_sig = [(k, v.default) for k, v in actual_sig.parameters.items()]
    assert actual_sig == expected_sig


def test_tabulate_signature():
    "API: tabulate() type signature is unchanged"
    assert type(tabulate) is type(lambda: None)  # noqa
    expected_sig = [
        ("tabular_data", _empty),
        ("headers", ()),
        ("tablefmt", "simple"),
        ("floatfmt", "g"),
        ("intfmt", ""),
        ("numalign", "default"),
        ("stralign", "default"),
        ("missingval", ""),
        ("showindex", "default"),
        ("disable_numparse", False),
        ("colglobalalign", None),
        ("colalign", None),
        ("preserve_whitespace", False),
        ("maxcolwidths", None),
        ("headersglobalalign", None),
        ("headersalign", None),
        ("rowalign", None),
        ("maxheadercolwidths", None),
        ("break_long_words", True),
        ("break_on_hyphens", True),
    ]
    _check_signature(tabulate, expected_sig)


def test_simple_separated_format_signature():
    "API: simple_separated_format() type signature is unchanged"
    assert type(simple_separated_format) is type(lambda: None)  # noqa
    expected_sig = [
        ("separator", _empty),
        ("kwargs", _empty),
    ]
    _check_signature(simple_separated_format, expected_sig)
