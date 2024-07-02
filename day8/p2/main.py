

INPUT_FILE = "input.text"
INSTRUCTIONS = []
PATH = {}
import math

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

    # Find all starting positions (because we're a ghost in the 4th dimension)
    initial_positions = []
    for pos in PATH:
        if pos[2] == 'A':
            initial_positions.append(pos)

    # Find how many steps for each ghost to get to Z
    steps_to_finish = []
    for pos in initial_positions:

        steps = 0
        done = False
        while True:

            for instruction in INSTRUCTIONS:

                pos = PATH[pos][instruction]

                if pos[2] == 'Z':
                    done = True
                    break

                steps += 1

            if done:
                steps_to_finish.append(steps + 1)
                break

    print(f'Steps to finish: {math.lcm(*steps_to_finish)}')




if __name__ == "__main__":
    main()
