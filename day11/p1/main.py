import math
import copy
INPUT_FILE = "test.text"

class Point:
    x: int
    y: int

    def __init__(self, x: int , y: int):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.x)

    def __str__(self) -> str:
        return f'P({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def _length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalise(self) -> None:
        self.x /= self._length()
        self.y /= self._length()

def distance(p1: Point, p2: Point) -> int:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def main():

    with open(INPUT_FILE, 'r') as file:
        universe = file.readlines()

    # Shave off the newlines
    for i in range(0, len(universe)):
        # print(universe[i])
        universe[i] = universe[i][:-1]
        # print(universe[i])

    expanded_universe: list[str] = universe.copy()
    added_rows = 0
    # Expand it!
    for y in range(0, len(universe)):
        row: str = universe[y]

        # If no galaxies found in row
        if row.find('#') == -1:
            expanded_universe.insert(y + added_rows, row)
            added_rows += 1

    # for r in expanded_universe:
    #         print(r)

    # print()

    row_n = len(expanded_universe)
    added_cols = 0
    for column_i in range(0, len(expanded_universe[0])):
        no_galaxy = True

        for y in range(0, row_n):
            if expanded_universe[y][column_i + added_cols] == '#':
                no_galaxy = False
                break

        if no_galaxy:
            for y in range(0, row_n):
                l = list(expanded_universe[y])
                l.insert(column_i + added_cols, '.')
                expanded_universe[y] = ''.join(l)
            added_cols += 1


    # for r in expanded_universe:
    #     print(r)

    # now find lengths or something

    # oh but first find galaxies
    galaxies: list[Point] = []
    universe = expanded_universe
    n_y = len(universe)

    for y in range(0, n_y):
        row = universe[y]

        for x in range(0, len(row)):
            if row[x] == '#':
                galaxies.append(Point(x, y))

    for p in galaxies:
        print(p)

    # ok now find lengths or something
    total = 0
    g1_i = 0
    for g1 in galaxies:

        # print(g1)

        g2_i = 0
        for g2 in galaxies:
            steps = 0

            t = copy.copy(g1)
            # Get steps
            while t != g2:
                if t.x < g2.x:
                    t.x += 1
                    steps += 1
                elif t.x > g2.x:
                    t.x -= 1
                    steps += 1
                if t.y < g2.y:
                    t.y += 1
                    steps += 1
                elif t.y > g2.y:
                    t.y -= 1
                    steps += 1

                # if g1 == Point(5, 11):
                #     print(f't {t} g2 {g2}')

            total += steps
            # print(f'{steps} from g{g1} to g{g2}')
            g2_i += 1
        g1_i += 1



    print(f'Sum is {total/2}')





if __name__ == '__main__':
    main()
