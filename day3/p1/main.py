with open("input.text", 'r') as f:
    contents = f.read().split("\n")

sum_of_parts = 0

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

                check_char = contents[index - 1][check_index]

                if check_char != "." and not check_char.isnumeric():
                    sum_of_parts += int(part_number)
                    print(f"Added {part_number}, symbol at ({index - 1}, {check_index}), symbol = \"{check_char}\"")
                    symbol = True
                    break
        if symbol:
            continue

        # Check current line
        if start_index != part_index:
            if line[start_index] != "." and not line[start_index].isnumeric():
                sum_of_parts += int(part_number)
                print(f"Added {part_number}, symbol at ({index}, {start_index}), symbol = \"{line[start_index]}\"")
                continue
        
        if end_index != part_index + length - 1:
            if line[end_index - 1] != "." and not line[end_index - 1].isnumeric():
                sum_of_parts += int(part_number)
                print(f"Added {part_number}, symbol at ({index}, {end_index - 1}), symbol = \"{line[end_index - 1]}\"")
                continue

        # Check line bellow
        if index != (len(contents) - 1):
            for check_index in range(start_index, end_index):

                check_char = contents[index + 1][check_index]

                if check_char != "." and not check_char.isnumeric():
                    sum_of_parts += int(part_number)
                    print(f"Added {part_number}, symbol at ({index + 1}, {check_index}), symbol = \"{check_char}\"")
                    symbol = True
                    break
        if symbol:
            continue

print(f"Sum of engine parts: {sum_of_parts}")
