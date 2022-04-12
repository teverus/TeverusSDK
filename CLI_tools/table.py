"""
* верхняя линия
* нижняя линия
* index_columns
* thead
* перекрестья
"""

# noinspection PyAttributeOutsideInit


# class Table:
#     def __init__(self, rows: list, table_width: int = None, center: bool = True):
#         rows_ = rows[:]
#         self.rows = rows_ if isinstance(rows_, list) else [rows_]
#         self.rows = [e if isinstance(e, list) else [e] for e in self.rows]
#         self.table_width = table_width
#         self.center = center
#         self.table_balance = 0
#         self.need_to_balance = 0
#         self.col_balance = 0
#
#         self.force_string_type_on_the_data()
#         self.calculate_column_widths()
#         self.calculate_available_width()
#         self.calculate_equal_column_width()
#
#         self.create_rows()
#
#         self.print_the_table()
#
#     def force_string_type_on_the_data(self):
#         for row in self.rows:
#             for index, line in enumerate(row):
#                 row[index] = str(line)
#
#     def calculate_column_widths(self):
#         self.column_lengths = {column: 0 for column in range(len(self.rows[0]))}
#         for row in self.rows:
#             for index, line in enumerate(row):
#                 if len(line) > self.column_lengths[index]:
#                     self.column_lengths[index] = len(line)
#
#         self.columns_sum = sum(list(self.column_lengths.values()))
#
#     def calculate_available_width(self):
#         self.col_number = len(self.rows[0])
#         walls = self.col_number - 1
#         inner_padding = 2 * self.col_number
#         self.available_width = self.table_width - walls - inner_padding
#
#     def calculate_equal_column_width(self):
#         self.equal_width = int(self.available_width / self.col_number)
#
#     def create_rows(self):
#         table_diff = self.available_width - self.equal_width * self.col_number
#         column_lengths = list(self.column_lengths.values())
#         big_col = [c for c in column_lengths if c > self.equal_width]
#
#         for row_index, row in enumerate(self.rows):
#             for col_index, column in enumerate(row):
#                 current_column_width = self.column_lengths[col_index]
#
#                 padding = self.equal_width
#
#                 # If table_width is too big
#                 if self.table_balance != table_diff:
#                     if self.available_width != (self.equal_width * self.col_number):
#                         padding = self.equal_width + 1
#                         self.table_balance += 1
#
#                 # If one of the columns is bigger than an equal width column
#                 elif big_col:
#                     if current_column_width > self.equal_width:
#                         max_col = max(column_lengths)
#                         rem_length = sum([c for c in column_lengths if c != max_col])
#                         max_column_width = self.available_width - rem_length
#
#                         condition1 = current_column_width > max_column_width
#                         condition2 = current_column_width == max_col
#                         if condition1 and condition2:
#                             too_much = current_column_width - max_column_width
#                             middle = int(max_column_width / 2)
#                             part1 = column[:middle]
#                             part2 = column[middle + 1 + too_much :]
#                             column = f"{part1}~{part2}"
#                             padding = max_column_width
#                         else:
#                             padding = current_column_width
#
#                         extra_w = current_column_width - self.equal_width
#                         self.need_to_balance += extra_w
#                     else:
#                         left_to_cover = self.need_to_balance - self.col_balance
#                         if left_to_cover:
#                             small_columns = self.col_number - len(big_col)
#                             try_to_cover = ceil(self.need_to_balance / small_columns)
#                             if try_to_cover < left_to_cover:
#                                 padding = self.equal_width - try_to_cover
#                                 self.col_balance += try_to_cover
#                             else:
#                                 padding = self.equal_width - left_to_cover
#                                 self.col_balance += left_to_cover
#
#                 alignment = column.center if self.center else column.ljust
#                 row[col_index] = alignment(padding, "*")
#
#             self.rows[row_index] = f' {" | ".join(row)} '
#
#     def print_the_table(self):
#         self.table_top = f"{'-' * self.table_width}"
#         self.table_bot = f"{'-' * self.table_width}"
#         print(self.table_top)
#         [print(row) for row in self.rows]
#         print(self.table_bot)
#
#         self.table = [self.table_top] + self.rows + [self.table_bot]


# noinspection PyAttributeOutsideInit
"""class Table2:
    def __init__(self, rows: list, table_width: int = None, center: bool = True):
        rows_ = rows[:]
        self.rows = rows_ if isinstance(rows_, list) else [rows_]
        self.rows = [e if isinstance(e, list) else [e] for e in self.rows]
        self.width_total = table_width
        self.center = center
        self.balance_remaining = 0
        self.fit_columns_left = 0

        self.force_string_type_on_the_data()
        self.calculate_column_widths()
        self.calculate_available_width()
        self.calculate_width_even()
        self.column_analysis()

        self.calculate_rows()

        self.print_the_table()

    def force_string_type_on_the_data(self):
        for row in self.rows:
            for index, line in enumerate(row):
                row[index] = str(line)

    def calculate_column_widths(self):
        self.column_lengths = {column: 0 for column in range(len(self.rows[0]))}
        for row in self.rows:
            for index, line in enumerate(row):
                if len(line) > self.column_lengths[index]:
                    self.column_lengths[index] = len(line)

        self.columns_sum = sum(list(self.column_lengths.values()))

    def calculate_available_width(self):
        self.column_number = len(self.rows[0])

        self.walls = self.column_number - 1
        self.inner_padding = 2 * self.column_number
        self.width_available = self.width_total - self.walls - self.inner_padding

    def calculate_width_even(self):
        self.width_even = int(self.width_available / self.column_number)
        self.width_expected = self.width_even * self.column_number
        self.width_remainder = self.width_available - self.width_expected

    def column_analysis(self):
        self.table = {}
        for index, row in enumerate(self.rows):
            self.table[index] = {}
            for index_, column in enumerate(row):
                column_length = len(column)
                self.table[index][index_] = {"expected_length": len(column)}
                self.table[index][index_]["extra"] = self.width_even - column_length

        self.columns_that_fit = len(
            [c for c in list(self.column_lengths.values()) if c <= self.width_even]
        )
        self.fit_columns_left = self.columns_that_fit

        self.balance_available = 0
        for key, value in self.table.items():
            for key1, value1 in value.items():
                self.balance_available += value1["extra"]

        self.column_widest = max([c for c in list(self.column_lengths.values())])

    def calculate_rows(self):
        for index_row, row in enumerate(self.rows):
            for index_col, column in enumerate(row):

                padding = self.width_even
                this_column_extra = self.table[index_row][index_col]["extra"]

                if self.balance_available < 0:
                    if len(column) == self.column_widest:
                        diff = abs(self.balance_available)
                        max_possible_width = self.column_widest - diff
                        tail = column[-3:]
                        head = column[: (max_possible_width - len(tail) - 1)]
                        ellipsis = f"{head}~{tail}"
                        assert len(ellipsis) == max_possible_width
                        column = ellipsis

                    else:
                        if this_column_extra >= self.balance_available:
                            padding = len(column) + this_column_extra
                        else:
                            padding = 1

                elif this_column_extra < 0:
                    need_to_balance = abs(this_column_extra)
                    self.balance_remaining += need_to_balance

                    # TODO до какого предела?
                    padding = self.column_lengths[index_col]

                elif self.balance_remaining:
                    among_columns = self.balance_remaining % self.fit_columns_left == 0
                    div = self.balance_remaining / self.fit_columns_left

                    if div > this_column_extra:
                        padding = len(column) + this_column_extra
                    elif among_columns:
                        div = int(div)
                        padding -= div
                        self.balance_remaining -= div
                    else:
                        in_col = int(self.balance_remaining / self.fit_columns_left)

                        change = in_col + 1
                        padding -= change
                        self.balance_remaining -= change

                    self.fit_columns_left -= 1

                if self.width_remainder:
                    padding += 1
                    self.width_remainder -= 1

                alignment = column.center if self.center else column.ljust
                row[index_col] = alignment(padding, "*")

            self.rows[index_row] = f' {" | ".join(row)}^'

    def print_the_table(self):
        self.table_top = f"{'-' * self.width_total}"
        self.table_bot = f"{'-' * self.width_total}"
        print(self.table_top)
        [print(row) for row in self.rows]
        print(self.table_bot)

        self.table = [self.table_top] + self.rows + [self.table_bot]"""


class Table3:
    def __init__(
        self,
        rows: list,
        table_width: int = None,
        center: bool = True,
        table_top_border: str = "-",
        table_bottom_border: str = "-",
    ):

        # Given values
        self.rows = rows if isinstance(rows, list) else [rows]
        self.rows = [e if isinstance(e, list) else [e] for e in self.rows]
        self.width_total = table_width
        self.center = center
        self.table_top_border = table_top_border
        self.table_bottom_border = table_bottom_border

        # Calculated values
        self.widths_max = {}
        self.walls = 0
        self.inner_padding = 0
        self.width_to_be_covered = 0
        self.widths_target = 0

        self.table = None

        # Preparing the table
        self.force_string_type_on_the_data()
        self.perform_column_analysis()
        self.calculate_paddings()
        self.calculate_columns()

        # Printing the table
        self.print_the_table()

    def force_string_type_on_the_data(self):
        for row in self.rows:
            for index, line in enumerate(row):
                row[index] = str(line)

    def perform_column_analysis(self):
        column_number = len(self.rows[0])

        self.widths_max = {index: 0 for index, _ in enumerate(self.rows[0])}
        for row in self.rows:
            for index, column in enumerate(row):
                if self.widths_max[index] < len(column):
                    self.widths_max[index] = len(column)

        self.walls = column_number - 1
        self.inner_padding = column_number * 2

        extra = self.walls + self.inner_padding
        self.width_to_be_covered = sum(self.widths_max.values()) + extra

    def calculate_paddings(self):
        if self.width_to_be_covered > self.width_total:
            raise Exception(
                f"[ERROR] You must use table_width at least {self.width_to_be_covered}"
            )

        elif self.width_to_be_covered < self.width_total:
            raise Exception("!!!!!!!")

        else:
            self.widths_target = self.widths_max

    def calculate_columns(self):
        for index_row, row in enumerate(self.rows):
            for index_col, column in enumerate(row):

                alignment = column.center if self.center else column.ljust
                row[index_col] = alignment(self.widths_target[index_col], "*")

            self.rows[index_row] = f' {" | ".join(row)}^'

    def print_the_table(self):
        table_top = self.table_top_border * self.width_total
        table_bottom = self.table_bottom_border * self.width_total

        print(table_top)
        [print(row) for row in self.rows]
        print(table_bottom)

        self.table = [table_top] + self.rows + [table_bottom]


def data(*args):
    columns = []
    for arg in args:
        string = ""
        for num in range(arg):
            number = num + 1 if num < 9 else num - 9
            string = f"{string}{str(number)}"
        columns.append(string)

    return [columns]


if __name__ == "__main__":
    # 14, 14, 6 // 38
    print("123456789|123456789|123456789|123456789|12345")
    # Table2(rows=data(1, 1, 1), table_width=20, center=False)
    Table3(
        rows=[
            [12345, "world", "pig"],
            [1, 123456, 1]
        ],
        table_width=22,
        center=False
    )
"""
"""
