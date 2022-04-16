import pytest as pytest

from CLI_tools.constants import *
from CLI_tools.table import data, Table


# @pytest.mark.parametrize(
#     "width, test",
#     [(38, TEST_1), (39, TEST_2), (40, TEST_3), (41, TEST_4), (42, TEST_5)],
# )
# def test_table_width(width, test):
#     print("")
#     assert Table(rows=data([10, 10, 10]), table_width=width, center=False).table == test
#
#
# @pytest.mark.parametrize(
#     "col, test",
#     [
#         ([10, 8, 8], TEST_6),
#         ([11, 8, 8], TEST_7),
#         ([12, 8, 8], TEST_8),
#         ([13, 8, 8], TEST_9),
#         ([14, 8, 8], TEST_10),
#         ([15, 8, 8], TEST_11),
#         ([16, 8, 8], TEST_12),
#         ([11, 11, 8], TEST_13),
#         ([14, 11, 6], TEST_14),
#         ([14, 12, 6], TEST_15),
#         ([14, 13, 6], TEST_16),
#         ([14, 9, 6], TEST_17)
#     ],
# )
# def test_column_width(col, test):
#     print("")
#     assert Table(rows=data(*col), table_width=38, center=False).table == test
#     # try:
#     #     assert Table2(rows=data(*col), table_width=38, center=False).table == test
#     # except AssertionError:
#     #     raise Exception(f"col = {col}")


def test1():
    table = Table(rows=data(1), table_width=38).table
    assert table == [
        "--------------------------------------",
        " 1*********************************** ",
        "--------------------------------------",
    ]


def test2():
    table = Table(rows=data([20, 12, 1]), table_width=38).table
    assert table == [
        "--------------------------------------",
        " 1234567890123~910 | 123456789012 | 1 ",
        "--------------------------------------",
    ]


# def test3():
#     table = Table(rows=data([1, 1, 1]), table_width=38).table
#     assert table == [
#         "--------------------------------------",
#         " 1********* | 1********* | 1********* ",
#         "--------------------------------------",
#     ]
