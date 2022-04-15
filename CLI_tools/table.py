"""
* index_columns
* thead
* перекрестья
"""


# noinspection PyAttributeOutsideInit
class Table:
    def __init__(
        self,
        rows: list,
        table_width: int = None,
        center: bool = False,
        default_alignment: str = "left",
        table_top_border: str = "-",
        table_bottom_border: str = "-",
    ):
        """
        * default_alignment can be "left" or "right"
        * if center is True, default_alignment isn't applied
        """

        # Given values
        self.rows = rows if isinstance(rows, list) else [rows]
        self.rows = [e if isinstance(e, list) else [e] for e in self.rows]
        self.width_total = table_width
        self.center = center
        self.alignment = default_alignment
        self.border_top = table_top_border
        self.border_bottom = table_bottom_border

        # Calculated values
        self.walls = 0
        self.inner_padding = 0
        self.extra = 0
        self.widths_max = {}
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
            value = min(self.widths_max.values())
        elif maximum:
            value = max(self.widths_max.values())
        else:
            raise Exception("[ERROR] You must choose either minimum or maximum")

        index = max([k for k, v in self.widths_max.items() if v == value])

        if minimum:
            self.widths_max[index] += 1
        elif maximum:
            self.widths_max[index] -= 1
        else:
            raise Exception("[ERROR] You must choose either minimum or maximum")

        self.width_to_be_covered = sum(self.widths_max.values()) + self.extra

    def calculate_columns(self):
        for index_row, row in enumerate(self.rows):
            for index_col, column in enumerate(row):
                column_width = len(column)
                target_width = self.widths_max[index_col]

                if column_width > target_width:
                    tail = column[-3:]
                    head = column[: (target_width - len(tail) - 1)]
                    column = f"{head}~{tail}"

                def_alignment = {"left": column.ljust, "right": column.rjust}
                align = column.center if self.center else def_alignment[self.alignment]

                row[index_col] = align(target_width, "*")

            self.rows[index_row] = f' {" | ".join(row)} '

    def print_the_table(self):
        table_top = self.border_top * self.width_total
        table_bottom = self.border_bottom * self.width_total

        print(table_top)
        [print(row) for row in self.rows]
        print(table_bottom)

        self.table = [table_top] + self.rows + [table_bottom]


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
    Table(rows=data([14, 17, 6], [1, 1, 1]), table_width=38)
