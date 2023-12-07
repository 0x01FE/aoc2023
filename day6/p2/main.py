
FILE_PATH = "input.text"

def main() -> None:
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()

    race_time: int = int(''.join(list(map(lambda x: x if x != " " else "", lines[0][5:]))))
    race_record_distance: int = int(''.join(list(map(lambda x: x if x != " " else "", lines[1][10:]))))

    win_combinations: int = 0
    for v in range(1, race_time):

        time_left: int = race_time - v
        distance: int = v * time_left

        if distance > race_record_distance:
            win_combinations += 1


    print(f"Win combinations: {win_combinations}")



if __name__ == "__main__":
    main()


