with open("input.text", 'r') as f:
    contents = f.read().split("\n")

sum_of_parts = 0

"""
{
    (1, 3) : [467, 35]
}
"""
gears = {}

for index, line in enumerate(contents):
    
    # Find numbers
    part_numbers = []
    num: bool = False
    num_index = None
    length = 0
    for char_index, char in enumerate(line):
        if char.isnumeric():
            if not num:
                num_index = char_index

            num = True
            length += 1
        else:
            if num:
                part_numbers.append((num_index, length, line[num_index:num_index + length]))
                num = False
                length = 0

    if num:
        part_numbers.append((num_index, length, line[num_index:num_index + length]))

    if part_numbers:
        print(f"index {index}, {part_numbers}")

    # Check for symbols
    for part_index, part_length, part_number in part_numbers:

        symbol = False

        minus = 1 if part_index != 0 else 0
        add = 1 if part_index + length != len(line) else 0
        start_index = part_index - minus
        end_index = part_index + part_length + add

        # Check line above
        if index != 0:
            for check_index in range(start_index, end_index):

                coords = (index - 1, check_index)
                x, y = coords
                check_char = contents[x][y]

                if check_char == "*":
                    if coords in gears:
                        gears[coords].append(part_number)
                    else:
                        gears[coords] = [part_number]

                    symbol = True
                    break
        if symbol:
            continue

        # Check current line
        if start_index != part_index:
            if line[start_index] == "*":
                coords = (index, start_index)

                check_char = line[start_index]

                if check_char == "*":
                    if coords in gears:
                        gears[coords].append(part_number)
                    else:
                        gears[coords] = [part_number]

                continue

        if end_index != part_index + length - 1:
            if line[end_index - 1] == "*":
                coords = (index, end_index - 1)

                check_char = line[end_index - 1]

                if check_char == "*":
                    if coords in gears:
                        gears[coords].append(part_number)
                    else:
                        gears[coords] = [part_number]

                continue

        # Check line bellow
        if index != (len(contents) - 1):
            for check_index in range(start_index, end_index):

                coords = (index + 1, check_index)
                x, y = coords

                check_char = contents[x][y]

                if check_char == "*":
                    if coords in gears:
                        gears[coords].append(part_number)
                    else:
                        gears[coords] = [part_number]

                    symbol = True
                    break
        if symbol:
            continue


sum_of_gear_ratios = 0
for gear in gears:
    if len(gears[gear]) == 2:
        gear_ratio = int(gears[gear][0]) * int(gears[gear][1])
        print(gear_ratio)
        sum_of_gear_ratios += gear_ratio

print(f"Sum of gear ratios: {sum_of_gear_ratios}")