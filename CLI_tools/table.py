"""
TODO
* column_alignment
* верхняя линия
* нижняя линия

* index_columns
* thead
* перекрестья
"""


# noinspection PyAttributeOutsideInit
class Table:
    def __init__(self, rows: list, table_width: int = None, center: bool = True):
        self.rows = rows if isinstance(rows, list) else [rows]
        self.table_width = table_width
        self.center = center

        self.force_string_type_on_the_data()
        self.calculate_the_widest_column_and_its_column_index()
        self.calculate_equal_column_width_and_remainder_if_any()

        self.create_rows()

        self.print_the_table()

    def force_string_type_on_the_data(self):
        for row in self.rows:
            row = row if isinstance(row, list) else [row]
            for index, line in enumerate(row):
                row[index] = str(line)

    def calculate_the_widest_column_and_its_column_index(self):
        longest_string = max([len(str(row)) for row in self.rows])
        the_longest_line = [row for row in self.rows if len(str(row)) == longest_string]
        self.max_col_index = 0
        self.max_width = 0
        for element in the_longest_line:
            for index, line in enumerate(element, 1):
                if index > self.max_col_index and len(line) > self.max_width:
                    self.max_col_index = index - 1
                    self.max_width = len(line)

    def calculate_equal_column_width_and_remainder_if_any(self):
        number_of_columns = len(self.rows[0])
        walls = number_of_columns - 1
        inner_padding = 2 * number_of_columns
        actual_width = self.table_width - walls - inner_padding

        self.equal_width = int(actual_width / number_of_columns)
        self.remainder = actual_width - (self.equal_width * number_of_columns)

    def create_rows(self):
        for row_index, row in enumerate(self.rows):
            small_w = self.equal_width + (self.equal_width - self.max_width)
            row = row if isinstance(row, list) else [row]
            for index, line in enumerate(row):
                if self.max_width > self.equal_width:
                    w = self.max_width if index == self.max_col_index else small_w
                else:
                    w = self.equal_width
                con1 = self.remainder == 1 and index == 0
                con2 = self.remainder == 2 and index in [0, 1]
                if self.center:
                    row[index] = line.center(w + 1 if any([con1, con2]) else w, "*")
                else:
                    row[index] = line.ljust(w + 1 if any([con1, con2]) else w, "*")

            self.rows[row_index] = f' {" | ".join(row)} '

    def print_the_table(self):
        print(f"{'-' * self.table_width}")
        [print(row) for row in self.rows]
        print(f"{'-' * self.table_width}")


if __name__ == "__main__":
    animals = ["Z", "123456789|123", "Z"]
    numbers = ["Z", "Z", "123456789|123"]
    chars = ["123456789|123", "Z", "Z"]
    data = [
        [
            animal,
            number,
            char
        ]
        for animal,
            number,
            char
        in zip(
            animals,
            numbers,
            chars
        )
    ]

    print("123456789|123456789|123456789|123456789|123456789|123456789|")
    Table(rows=data, table_width=47)
