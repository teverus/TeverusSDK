"""
TODO
* !!! ЕСЛИ СУММА КОЛОНОК БОЛЬШЕ self.actual_width
* верхняя линия
* нижняя линия

* index_columns
* thead
* перекрестья
"""


# noinspection PyAttributeOutsideInit
class Table:
    def __init__(self, rows: list, table_width: int = None, center: bool = True):
        rows_ = rows[:]
        self.rows = rows_ if isinstance(rows_, list) else [rows_]
        self.table_width = table_width
        self.center = center
        self.balance = 0
        self.need_to_balance = 0

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
        self.equal_w = int(self.available_width / self.col_number)

    def create_rows(self):
        is_perfect = self.available_width == self.columns_sum
        optimal = self.equal_w * self.col_number
        table_diff = self.available_width - optimal
        column_diff = [c for c in list(self.column_lengths.values()) if c > self.equal_w]

        for row_index, row in enumerate(self.rows):
            row = row if isinstance(row, list) else [row]

            for col_index, line in enumerate(row):
                if is_perfect:
                    padding = self.equal_w
                else:
                    if self.balance != table_diff:
                        if self.available_width == (self.equal_w * self.col_number):
                            padding = self.equal_w
                        else:
                            padding = self.equal_w + 1
                            self.balance += 1
                    else:
                        if column_diff:
                            if self.column_lengths[col_index] > self.equal_w:
                                # TODO должен быть предел
                                padding = self.column_lengths[col_index]
                                extra_w = self.column_lengths[col_index] - self.equal_w
                                self.need_to_balance = extra_w
                            else:
                                if self.balance != self.need_to_balance:
                                    padding = self.equal_w - 1
                                    self.balance += 1
                        else:
                            padding = self.equal_w

                # line = f"{line[:12]}~" if len(line) > padding else line
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
    Table(rows=data(12, 8, 8), table_width=38, center=False)
