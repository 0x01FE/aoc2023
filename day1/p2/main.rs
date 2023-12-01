use std::fs;

fn find_first(line: &str) -> (u32, usize)
{
    let mut value = 0;

    let mut lowest_index = usize::MAX;

    let numbers = vec!["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let numbers_values = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];

    for i in 0..numbers.len()
    {
        let found_index = line.find(numbers[i]);
        let found_index_value = match found_index {
            None => continue,
            Some(found_index) => found_index
        };

        if found_index_value <= lowest_index
        {
            value = numbers_values[i];
            lowest_index = found_index_value;
        }
    }

    return (value, lowest_index);
}

fn find_last(line: &str) -> (u32, usize)
{
    let mut value = 0;

    let mut lowest_index = usize::MIN;

    let numbers = vec!["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let numbers_values = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];

    for i in 0..numbers.len()
    {
        let found_index = line.rfind(numbers[i]);
        let found_index_value = match found_index {
            None => continue,
            Some(found_index) => found_index
        };

        if found_index_value >= lowest_index
        {
            value = numbers_values[i];
            lowest_index = found_index_value;
        }
    }

    return (value, lowest_index);
}

fn main()
{
    let file_path: &str = "./input.text";

    let contents = fs::read_to_string(file_path)
        .unwrap();

    let mut sum:i32 = 0;

    for line in contents.lines()
    {
        println!("{line}");

        let mut first: u32 = 10;
        let mut first_index: usize = usize::MAX;
        let mut last: u32 = 0;
        let mut last_index: usize = usize::MIN;

        let mut index: usize = 0;
        for character in line.chars()
        {
            if character.is_ascii_digit()
            {
                let value = character.to_digit(10).unwrap();
                if first == 10
                {
                    first = value;
                    first_index = index;
                }
                last = value;
                last_index = index;
            }
            index += 1;
        }

        let (l_value, l_index) = find_last(line);
        if l_index > last_index
        {
            last = l_value;
        }
        let (f_value, f_index) = find_first(line);
        if f_index < first_index
        {
            first = f_value;
        }

        let result = first.to_string() + &last.to_string();

        println!("Sum of line {result}.");

        sum += result.parse::<i32>().unwrap();

    }

    println!("Sum: {sum}");
}
