INPUT_FILE = "input.text"

def extrapolate_value(line: str) -> int:

    initial_values: list[int] = [int(v) for v in line.split(' ')]

    values = [initial_values]

    # Loop until last thing is all 0, 0, 0...
    while len(values[-1]) != values[-1].count(0):
        new_values: list[int] = []

        current_row: list[int] = values[-1]
        for value_index in range(1, len(current_row)):
            new_values.append(current_row[value_index] - current_row[value_index - 1])

        values.append(new_values)

    # Now we can extrapolate our new values, starting from the bottom
    for row_index in reversed(range(0, len(values) - 2)): # -1 because we know the last row is all 0's
        current_row: list[int] = values[row_index]
        row_bellow: list[int] = values[row_index + 1]

        values[row_index].insert(0, current_row[0] - row_bellow[0])

    return values[0][0] # Return last value of the first row


def main():

    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()

    sum_of_values = 0
    for line in lines:
        extrapolated_history_value: int = extrapolate_value(line)

        sum_of_values += extrapolated_history_value

    print(f'Sum of extrapolated values: {sum_of_values}')




if __name__ == "__main__":
    main()



