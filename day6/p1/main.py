
FILE_PATH = "input.text"

def main() -> None:
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()

    race_times: list[int] = list(map(lambda x: int(x), lines[0].split()[1:]))
    race_record_distances: list[int] = list(map(lambda x: int(x), lines[1].split()[1:]))

    win_combinations: list[int] = []
    for index, time in enumerate(race_times):

        wins: int = 0

        for v in range(1, time):

            time_left: int = time - v
            distance: int = v * time_left

            if distance > race_record_distances[index]:
                wins += 1

        win_combinations.append(wins)

    product: int = win_combinations[0]
    for combo in win_combinations[1:]:
        product *= combo

    print(f"Product of combinations: {product}")



if __name__ == "__main__":
    main()


