use std::{fs, vec};

const FILE_PATH: &str = "./input.text";

fn process_line(line: &str) -> i32
{
    let mut cards_won = 0;

    // Line processing
    let line_halves: Vec<&str> = line.split(" | ").collect();

    let first_half: Vec<&str> = line_halves[0].split(": ").collect();

    let winning_numbers: Vec<&str> = first_half[1].split(" ").filter(|num| !num.is_empty()).collect();

    let my_numbers = line_halves[1].split(" ").filter(|num| !num.is_empty());

    for number in my_numbers
    {
        if winning_numbers.contains(&number)
        {
            cards_won += 1;
        }
    }

    return cards_won;
}

fn main() {
    let contents = fs::read_to_string(FILE_PATH)
    .unwrap();

    let lines: Vec<&str> = contents.lines().collect();

    let mut cards_won_sum: i64 = 0;
    let mut card_values: Vec<(usize, i32)> = Vec::new();

    for index in 0..lines.len()
    {
        let mut temp_vec = vec![(index, process_line(lines[index]))];
        card_values.append(&mut temp_vec);

    }

    let mut cards_won: Vec<(usize, i32)> = card_values.clone();

    while !cards_won.is_empty()
    {
        let mut temp_cards_won: Vec<(usize, i32)> = Vec::new();
        for (index, cards_won_value) in cards_won.clone()
        {
            cards_won_sum += 1;
            for i in (index + 1)..(index + 1 + cards_won_value as usize)
            {
                let mut temp_vec: Vec<(usize, i32)> = vec![(i, card_values[i].1)];
                temp_cards_won.append(&mut temp_vec);
            }
        }

        cards_won = temp_cards_won;
    }


    println!("Total cards won: {cards_won_sum}");
}