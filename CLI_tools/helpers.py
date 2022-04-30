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
