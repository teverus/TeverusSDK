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

        self.force_string_type_on_the_data()
        self.calculate_column_widths()
        self.calculate_available_width()
        self.calculate_equal_column_width_and_remainder_if_any()

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
        self.max_width = max(list(self.column_lengths.values()))

    def calculate_available_width(self):
        self.col_number = len(self.rows[0])
        walls = self.col_number - 1
        inner_padding = 2 * self.col_number
        self.available_width = self.table_width - walls - inner_padding

    def calculate_equal_column_width_and_remainder_if_any(self):
        self.equal_w = int(self.available_width / self.col_number)
        self.remainder = self.available_width - (self.equal_w * self.col_number)

    def create_rows(self):
        is_perfect = self.available_width == self.columns_sum
        optimal = self.equal_w * self.col_number
        diff = self.available_width - optimal

        for row_index, row in enumerate(self.rows):
            row = row if isinstance(row, list) else [row]

            for col_index, line in enumerate(row):
                if is_perfect:
                    padding = self.equal_w
                else:
                    if self.balance != diff:
                        if self.available_width == (self.equal_w * self.col_number):
                            padding = self.equal_w
                        else:
                            padding = self.equal_w + 1
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


if __name__ == "__main__":
    col1 = ["1234567890"]
    col2 = ["1234567890"]
    col3 = ["1234567890"]
    data = [[c1, c2, c3] for c1, c2, c3 in zip(col1, col2, col3)]

    # print("123456789|123456789|123456789|123456789|123456789|123456789|")
    Table(rows=data, table_width=48, center=False)
