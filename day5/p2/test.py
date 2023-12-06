class Range:
    start: int
    end: int

    def __init__(self, s: int, e: int):
        self.start = s
        self.end = e

    def contains(self, key) -> tuple | None:
        start, end = (key.start, key.end)

        if start > self.end or end <= self.start:
            return None

        start_value = start if self.start <= start and start <= self.end else self.start
        end_value = end if self.end >= end and end >= self.start else self.end

        return Range(start_value, end_value)

    def __str__(self) -> str:
        return f'({self.start}, {self.end})'



r = Range(1, 5)
r2 = Range(2, 3)

print(r.contains(r2))



