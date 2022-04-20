"""
"""


# noinspection PyAttributeOutsideInit
class Table:
    def __init__(
        self,
        rows: list,
        center: bool = False,
        default_alignment: str = "left",

        headers: list = (),
        headers_top_border: str = "-",
        headers_centered: bool = False,

        table_width: int = None,
        show_index: bool = True,
        table_top_border: str = "-",
        table_bottom_border: str = "-",
    ):
        """
        * default_alignment can be "left" or "right"
        * if center is True, default_alignment isn't applied
        """

        # === Given values

        # Rows
        self.rows = rows if isinstance(rows, list) else [rows]
        self.rows = [e if isinstance(e, list) else [e] for e in self.rows]

        # Headers
        self.headers = [headers]
        self.headers_top_border = headers_top_border
        self.headers_centered = headers_centered

        # Table
        self.width_total = table_width
        self.center = center
        self.alignment = default_alignment
        self.show_index = show_index

        self.border_top = table_top_border
        self.border_bottom = table_bottom_border

        # === Calculated values
        self.walls = 0
        self.inner_padding = 0
        self.extra = 0
        self.widths_max = {}
        self.width_to_be_covered = 0
        self.widths_target = 0
        self.width_index = len(str(len(self.rows)))

        self.table = []

        # === Preparing the table
        self.force_string_type_on_the_data()
        self.perform_width_analysis()
        self.calculate_paddings()
        self.calculate_columns()

        # === Printing the table
        self.print_the_table()

    def force_string_type_on_the_data(self):
        for row in self.rows:
            for index, line in enumerate(row):
                row[index] = str(line)

    def perform_width_analysis(self):
        column_number = len(self.rows[0])
        column_number = column_number + 1 if self.show_index else column_number

        self.widths_max = {index: 0 for index, _ in enumerate(self.rows[0])}
        for row in self.headers + self.rows:
            for index, column in enumerate(row):
                if self.widths_max[index] < len(column):
                    self.widths_max[index] = len(column)

        if self.show_index:
            self.widths_max[-1] = self.width_index

        self.walls = column_number - 1
        self.inner_padding = column_number * 2

        self.extra = self.walls + self.inner_padding
        self.width_to_be_covered = sum(self.widths_max.values()) + self.extra

    def calculate_paddings(self):
        if self.width_to_be_covered > self.width_total:
            while self.width_to_be_covered != self.width_total:
                self.adjust_widths(maximum=True)

        elif self.width_to_be_covered < self.width_total:
            while self.width_to_be_covered != self.width_total:
                self.adjust_widths(minimum=True)

    def adjust_widths(self, minimum=False, maximum=False):
        if minimum:
            value = min([v for k, v in self.widths_max.items() if k != -1])
        elif maximum:
            value = max(self.widths_max.values())
        else:
            raise Exception("[ERROR] You must choose either minimum or maximum")

        index = max([k for k, v in self.widths_max.items() if k != -1 and v == value])

        if minimum:
            self.widths_max[index] += 1
        elif maximum:
            self.widths_max[index] -= 1
        else:
            raise Exception("[ERROR] You must choose either minimum or maximum")

        self.width_to_be_covered = sum(self.widths_max.values()) + self.extra

    def calculate_columns(self):
        for element in (self.headers, self.rows):
            self.create_columns(element)

    def create_columns(self, some_list):
        for index_row, row in enumerate(some_list):
            for index_col, column in enumerate(row):
                column_width = len(column)
                target_width = self.widths_max[index_col]

                if column_width > target_width:
                    tail = column[-3:]
                    head = column[: (target_width - len(tail) - 1)]
                    column = f"{head}~{tail}"

                # TODO центрирование для шапки таблицы
                # TODO upper для шапки таблицы
                def_alignment = {"left": column.ljust, "right": column.rjust}
                align = column.center if self.center else def_alignment[self.alignment]

                row[index_col] = align(target_width, "*")

            # TODO возможность задавать wall
            index = f" {str(index_row + 1).rjust(self.width_index)} |"
            rows = f" {' | '.join(row)} "

            if [row] == self.headers:
                if row:
                    index = index.replace("1", "#")
                    table_head = f"{index}{rows}" if self.show_index else rows
                    self.headers[index_row] = table_head
            else:
                some_list[index_row] = f"{index}{rows}" if self.show_index else rows

    def print_the_table(self):
        headers = self.headers[0]
        headers_top = self.headers_top_border * self.width_total if headers else ""
        table_top = self.get_table_top()
        table_bottom = self.border_bottom * self.width_total

        if headers:
            print(headers_top)
            print(headers)
            [self.table.append(element) for element in [headers_top, headers]]
        print(table_top)
        [print(row) for row in self.rows]
        print(table_bottom)

        [self.table.append(e) for e in [table_top, *self.rows, table_bottom]]

    def get_table_top(self):
        if self.headers == [()]:
            return self.border_top * self.width_total
        else:
            if self.show_index:
                all_but_index = [v for k, v in self.widths_max.items() if k != -1]
                widths = [f"{self.border_top * w}" for w in all_but_index]
                columns = ["-"] + widths
            else:
                columns = [f"{self.border_top * w}" for w in self.widths_max.values()]
            columns_with_walls = f"{self.border_top}+{self.border_top}".join(columns)
            border_full = f"{self.border_top}{columns_with_walls}{self.border_top}"
            return border_full


# TODO remove
def data(*args):
    columns = []
    for arg in args:
        arg = [arg] if not isinstance(arg, list) else arg

        column = []
        for element in arg:
            string = ""
            for num in range(element):
                number = num + 1 if num < 9 else num - 9
                string = f"{string}{str(number)}"
            column.append(string)
        columns.append(column)

    return columns


if __name__ == "__main__":
    aaa = Table(
        rows=data(
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            # [1, 1, 1],
        ),
        headers=["Badger", "Racoon", "Pig"],
        headers_centered=True,
        table_width=38,
        # show_index=False,
    ).table
