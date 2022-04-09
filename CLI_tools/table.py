"""
* верхняя линия
* нижняя линия
* index_columns
* thead
* перекрестья
"""

from math import ceil


# noinspection PyAttributeOutsideInit
class Table:
    def __init__(self, rows: list, table_width: int = None, center: bool = True):
        rows_ = rows[:]
        self.rows = rows_ if isinstance(rows_, list) else [rows_]
        self.table_width = table_width
        self.center = center
        self.table_balance = 0
        self.need_to_balance = 0
        self.col_balance = 0

        self.force_string_type_on_the_data()
        self.calculate_column_widths()
        self.calculate_available_width()
        self.calculate_equal_column_width()

        self.create_rows()

        self.print_the_table()

    def force_string_type_on_the_data(self):
        for row in self.rows:
            row = row if isinstance(row, list) else [row]
            for index, line in enumerate(row):
                row[index] = str(line)

    def calculate_column_widths(self):
        self.column_lengths = {column: 0 for column in range(len(self.rows[0]))}
        for row in self.rows:
            row = row if isinstance(row, list) else [row]
            for index, line in enumerate(row):
                if len(line) > self.column_lengths[index]:
                    self.column_lengths[index] = len(line)

        self.columns_sum = sum(list(self.column_lengths.values()))

    def calculate_available_width(self):
        self.col_number = len(self.rows[0])
        walls = self.col_number - 1
        inner_padding = 2 * self.col_number
        self.available_width = self.table_width - walls - inner_padding

    def calculate_equal_column_width(self):
        self.equal_width = int(self.available_width / self.col_number)

    def create_rows(self):
        optimal = self.equal_width * self.col_number
        table_diff = self.available_width - optimal
        column_lengths = list(self.column_lengths.values())
        big_col = [c for c in column_lengths if c > self.equal_width]

        for row_index, row in enumerate(self.rows):
            row = row if isinstance(row, list) else [row]

            for col_index, line in enumerate(row):
                current_column_width = self.column_lengths[col_index]

                padding = self.equal_width

                if self.table_balance != table_diff:
                    if self.available_width == (self.equal_width * self.col_number):
                        padding = self.equal_width
                    else:
                        padding = self.equal_width + 1
                        self.table_balance += 1
                elif big_col:
                    if current_column_width > self.equal_width:
                        max_col = max(column_lengths)
                        rem_length = sum([c for c in column_lengths if c != max_col])
                        max_column_width = self.available_width - rem_length

                        if current_column_width > max_column_width:
                            too_much = current_column_width - max_column_width
                            middle = int(max_column_width/2)
                            part1 = line[:middle]
                            part2 = line[middle + 1 + too_much:]
                            line = f"{part1}~{part2}"
                            padding = max_column_width
                        else:
                            padding = current_column_width

                        extra_w = current_column_width - self.equal_width
                        self.need_to_balance += extra_w
                    else:
                        left_to_cover = self.need_to_balance - self.col_balance
                        if left_to_cover:
                            small_columns = self.col_number - len(big_col)
                            try_to_cover = ceil(self.need_to_balance / small_columns)
                            if try_to_cover < left_to_cover:
                                padding = self.equal_width - try_to_cover
                                self.col_balance += try_to_cover
                            else:
                                padding = self.equal_width - left_to_cover
                                self.col_balance += left_to_cover

                alignment = line.center if self.center else line.ljust
                row[col_index] = alignment(padding, "*")

            self.rows[row_index] = f' {" | ".join(row)} '

    def print_the_table(self):
        self.table_top = f"{'-' * self.table_width}"
        self.table_bot = f"{'-' * self.table_width}"
        print(self.table_top)
        [print(row) for row in self.rows]
        print(self.table_bot)

        self.table = [self.table_top] + self.rows + [self.table_bot]


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
    Table(rows=data(14, 11, 6), table_width=38, center=False)
