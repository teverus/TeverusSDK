import pytest as pytest

from CLI_tools.constants import *
from CLI_tools.table import Table


@pytest.fixture()
def data():
    col1 = ["1234567890"]
    col2 = ["1234567890"]
    col3 = ["1234567890"]
    return [[c1, c2, c3] for c1, c2, c3 in zip(col1, col2, col3)]


@pytest.mark.parametrize(
    "width, test",
    [(38, TEST_1), (39, TEST_2), (40, TEST_3), (41, TEST_4), (42, TEST_5)],
)
def test_table_width(data, width, test):
    print("")
    assert Table(rows=data, table_width=width, center=False).table == test
