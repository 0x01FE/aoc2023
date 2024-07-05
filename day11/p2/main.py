import math
INPUT_FILE = "test.text"

I = 10

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

    def _abs(self) -> None:
        self.x = abs(self.x)
        self.y = abs(self.y)

def main():

    with open(INPUT_FILE, 'r') as file:
        universe = file.readlines()

    # Shave off the newlines
    for i in range(0, len(universe)):
        universe[i] = universe[i][:-1]

    # oh but first find galaxies
    galaxies: list[Point] = []
    n_y = len(universe)

    for y in range(0, n_y):
        row = universe[y]

        for x in range(0, len(row)):
            if row[x] == '#':
                galaxies.append(Point(x, y))

    print(f'galaxys {len(galaxies)}')

    # Check for expansion (y direction)
    expansions = 0
    for y in range(0, len(universe)):
        row: str = universe[y]

        if row.find('#') == -1:
            print(f'no galaxy at y {y}')
            for g in galaxies:
                if g.y > y + (expansions * I):
                    print(f'{g}, > {y}')
                    g.y += I
            expansions += 1

    for p in galaxies:
        print(p)
    print()

    # Check for expansions (x direction)
    expansions = 0
    for x in range(0, len(universe[0])):
        # no_galaxy = True

        # for g in galaxies:
        #     # print(f'{g.x} == {x}')
        #     if g.x == x + expansions:
        #         no_galaxy = False
        #         break

        # if no_galaxy:
        #     print(f'no galaxy on x {x}')
        #     for g in galaxies:
        #         if g.x > x + expansions:
        #             g.x += I
        #     expansions += 1

        no_galaxy = True

        for y in range(0, len(universe)):
            if universe[y][x] == '#':
                no_galaxy = False
                break

        if no_galaxy:
            print(f'no galaxy on x {x}')
            for g in galaxies:
                if g.x > x + (expansions * I):
                    print(f'{g} > {x}')
                    g.x += I
            expansions += 1


    for p in galaxies:
        print(p)

    # ok now find lengths or something
    total = 0
    for g1 in galaxies:
        for g2 in galaxies:

            if g2.y > g1.y:
                dy = g2.y - g1.y
            else:
                dy = g1.y - g2.y

            if g2.x > g1.x:
                dx = g2.x - g1.x
            else:
                dx = g1.x - g2.x

            total += dx + dy



    print(f'Sum is {total/2}')





if __name__ == '__main__':
    main()
