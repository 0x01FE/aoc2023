#!/bin/python3.12

FILE_PATH = "input.text"

class ConversionRange:
    target_start : int
    target_end : int
    source_start : int
    source_end : int
    translate : int

    def __init__(self, target_start : int, source_start : int, length : int):
        self.target_start = target_start
        self.source_start = source_start
        self.target_end = self.target_start + length
        self.source_end = self.source_start + length
        self.translate = self.target_start - self.source_start

    def __str__(self):
        print(f"Target start: {self.target_start}")
        print(f"Source start: {self.source_start}")
        print(f"Translate: {self.translate}")
        return ""



class Conversion:
    ranges : list[ConversionRange]

    def __init__(self):
        self.ranges = []
        pass

    def convert(self, num : int) -> int:
        for r in self.ranges:
            if num >= r.source_start and num <= r.source_end:
                return num + r.translate
        return num


def main() -> None:
    with open(FILE_PATH, 'r') as f:
        contents = f.read().split('\n')

    # Setup
    seeds: list[int] = []
    maps: dict[str, Conversion] = {}
    maps["seed-to-soil"] = Conversion()
    maps["soil-to-fertilizer"] = Conversion()
    maps["fertilizer-to-water"] = Conversion()
    maps["water-to-light"] = Conversion()
    maps["light-to-temperature"] = Conversion()
    maps["temperature-to-humidity"] = Conversion()
    maps["humidity-to-location"] = Conversion()

    current_conversion: str = ""

    # Parse the file
    for index, line in enumerate(contents):
        if index == 0:
            seeds_list: list[str] = line.split(": ")[1].split()
            for seed in seeds_list:
                seeds.append(int(seed))
            print(f"Seeds: {seeds}")
            continue

        if not line:
            continue

        if not line[0].isdigit():
            current_conversion = line[:-5]
            print(f"Current conversion: {current_conversion}")
            continue

        nums: list[int] = list(map(lambda x: int(x), line.split()))

        temp = ConversionRange(nums[0], nums[1], nums[2])
        print(temp)
        maps[current_conversion].ranges.append(temp)

    # Convert the seeds
    lowest_location: float = float('inf')
    for seed in seeds:
        temp = seed
        for key, value in maps.items():
            print(f"Mapping {temp} with {key}")
            temp = value.convert(temp)

        if temp < lowest_location:
            lowest_location = temp
        print(f"Location: {temp}")

    print(f"Lowest location: {lowest_location}")




if __name__ == "__main__":
    main()



