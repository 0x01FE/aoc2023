use std::fs;

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
        let mut last: u32 = 0;

        for character in line.chars()
        {
            if character.is_ascii_digit()
            {
                let value = character.to_digit(10).unwrap();
                if first == 10
                {
                    first = value;
                }
                last = value;
            }
        }

        let result = first.to_string() + &last.to_string();

        println!("Sum of line {result}.");

        sum += result.parse::<i32>().unwrap();

    }

    println!("Sum: {sum}");
}
