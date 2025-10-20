if __name__ == '__main__':
    count = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines_formatted = list()
        for line in lines:
            lines_formatted.append(list(line.strip()))
        matrix = lines_formatted
        columns_number = len(matrix)
        rows_number = len(matrix[0])
        possible_directions_to_check = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for row in range(columns_number):
            for column in range(rows_number):
                if matrix[row][column] == "X":
                    for row_movement, column_movement in possible_directions_to_check:
                        new_row = row + row_movement
                        new_column = column + column_movement
                        if 0 <= new_row < rows_number and 0 <= new_column < columns_number:
                            if matrix[new_row][new_column] == "M":
                                new_row = new_row + row_movement
                                new_column = new_column + column_movement
                                if 0 <= new_row < rows_number and 0 <= new_column < columns_number:
                                    if matrix[new_row][new_column] == "A":
                                        new_row = new_row + row_movement
                                        new_column = new_column + column_movement
                                        if 0 <= new_row < rows_number and 0 <= new_column < columns_number:
                                            if matrix[new_row][new_column] == "S":
                                                count += 1

    print(count)
