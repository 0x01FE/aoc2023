import math
INPUT_FILE = "input.text"


class Point:
    x: int
    y: int

    def __init__(self, x: int , y: int):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f'P({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

class PipeMap:
    pipe_map: list[str]
    start_position: Point
    bounds: Point

    def __init__(self, map_path: str):

        with open(map_path, 'r') as file:
            self.pipe_map = file.readlines()

        for i in range(0, len(self.pipe_map)):
            self.pipe_map[i] = self.pipe_map[i][:-1]

        max_y = len(self.pipe_map)
        for row in range(0, max_y):
            max_x = len(self.pipe_map[row])
            col = self.pipe_map[row].find('S')

            if col != -1:
                self.bounds = Point(max_x, max_y)
                self.start_position = Point(row, col)

    def in_bounds(self, p: Point) -> bool:
        return (p.x < self.bounds.x and p.y < self.bounds.y and p.x >= 0 and p.y >= 0)


directions = {
    8 : Point(-1, 0),
    9 : Point(-1, 1),
    6 : Point(0, 1),
    3 : Point(1, 1),
    2 : Point(1, 0),
    1 : Point(1, -1),
    4 : Point(0, -1),
    7 : Point(-1, -1)
}

pipe_directions = {
    '|' : [Point(-1, 0), Point(1, 0)],
    '-' : [Point(0, -1), Point(0, 1)],
    'L' : [Point(-1, 0), Point(0, 1)],
    'J' : [Point(-1, 0), Point(0, -1)],
    '7' : [Point(0, -1), Point(1, 0)],
    'F' : [Point(0, 1), Point(1, 0)],
    '.' : [],
    'S' : True
}

def main():

    pipe_map = PipeMap(INPUT_FILE)

    # Check around start
    next_directions = None
    current_pos: Point = pipe_map.start_position
    last_pos: Point = current_pos

    for d in directions:
        new_pos = pipe_map.start_position.add(directions[d])

        if pipe_map.in_bounds(new_pos):
            if char := pipe_directions[pipe_map.pipe_map[new_pos.x][new_pos.y]]:

                # Check if this pipe connects to start somehow
                good = False
                for d2 in char:
                    if new_pos.add(d2) == current_pos:
                        good = True
                        break

                if good:
                    current_pos = new_pos
                    next_directions = char
                    break

    steps = 1 # Because current pos isn't at start rn
    while current_pos != pipe_map.start_position:

        for direction in next_directions:
            potential_pos: Point = current_pos.add(direction)
            potential_directions: list[Point] = pipe_directions[pipe_map.pipe_map[potential_pos.x][potential_pos.y]]

            if pipe_map.in_bounds(potential_pos) and potential_pos != last_pos and potential_directions:
                last_pos = current_pos
                current_pos = potential_pos
                next_directions = potential_directions
                steps += 1
                break


    print(f'Loop finished, start found in {steps} steps')
    print(f'Critter is at {math.ceil(steps/2)}')



if __name__ == '__main__':
    main()
