use std::fs;


fn main() {
    let file_path = "./input.text";

    let contents = fs::read_to_string(file_path)
        .unwrap();

    let mut sum_of_points = 0;
    for line in contents.lines()
    {
        let line_halves: Vec<&str> = line.split(" | ").collect();

        let first_half: Vec<&str> = line_halves[0].split(": ").collect();

        let winning_numbers: Vec<&str> = first_half[1].split(" ").filter(|num| !num.is_empty()).collect();

        let my_numbers = line_halves[1].split(" ").filter(|num| !num.is_empty());

        let mut points = 0;
        for number in my_numbers
        {
            if winning_numbers.contains(&number)
            {
                if points == 0
                {
                    points = 1;
                }
                else
                {
                    points *= 2;
                }
            }
        }

        sum_of_points += points;
    }

    println!("Sum of points on cards: {sum_of_points}");
}
