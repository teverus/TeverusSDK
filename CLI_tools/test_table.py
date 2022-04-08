import pytest as pytest

from CLI_tools.constants import *
from CLI_tools.table import Table, data


@pytest.mark.parametrize(
    "width, test",
    [(38, TEST_1), (39, TEST_2), (40, TEST_3), (41, TEST_4), (42, TEST_5)],
)
def test_table_width(width, test):
    print("")
    assert Table(rows=data(10, 10, 10), table_width=width, center=False).table == test


@pytest.mark.parametrize(
    "col, test",
    [([11, 8, 8], TEST_6)]
)
def test_column_width(col, test):
    print("")
    assert Table(rows=data(*col), table_width=38, center=False).table == test
