

INPUT_FILE = "input.text"
INSTRUCTIONS = []
PATH = {}

def read_file() -> None:
    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()

    line_index = 0
    for line in lines:

        # This in our instruction line
        if line_index == 0:
            for char in line:
                if char == 'L':
                    INSTRUCTIONS.append(0)
                elif char == 'R':
                    INSTRUCTIONS.append(1)

        elif line_index != 1:
            source: str = line.split('=')[0].strip()

            dest = line.split('=')[1].strip()[1:-1].split(', ')

            PATH[source] = dest

        line_index += 1

def main() -> None:
    read_file()

    # print(PATH)

    pos = 'AAA'
    steps = 1
    while True:
        done = False

        for instruction in INSTRUCTIONS:
            pos = PATH[pos][instruction]

            if pos == 'ZZZ':
                done = True
                break

            steps += 1
        if done:
            break

    print(f'Steps taken: {steps}')




if __name__ == "__main__":
    main()
