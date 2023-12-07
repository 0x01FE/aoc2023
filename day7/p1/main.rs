use std::fs;
use std::collections::HashMap;

const FILE_PATH: &str = "./test.text";

enum HandType
{
    FiveOfKind,
    FourOfKind,
    FullHouse,
    ThreeOfKind,
    TwoPair,
    OnePair,
    HighCard
}

struct Hand
{
    value: String,
    bid: i32,
    hand_type: HandType
}

fn compare_hands(hand_1: Hand, hand_2: Hand) -> Hand
{
    let result: Hand;

    result
}

fn get_hand_type(hand: &str) //-> HandType
{
    // Parse hand into map
    let mut hand_values: HashMap<char, i32> = HashMap::new();
    for card in hand.chars()
    {
        match hand_values.get(&card) {
            Some(_) => { *hand_values.get_mut(&card).unwrap() += 1; },
            None => { hand_values.insert(card, 1); }
        }
    }

    // Decide HandType
    for (card, value) in &hand_values
    {
        
    }
}

fn card_value(card: &str) -> i32
{
    match card {
        "A" => 13,
        "K" => 12,
        "Q" => 11,
        "J" => 10,
        "T" => 9,
        "9" => 8,
        "8" => 7,
        "7" => 6,
        "6" => 5,
        "5" => 4,
        "4" => 3,
        "3" => 2,
        "2" => 1,
        _ => -1
    }
}

fn main()
{
    let contents = fs::read_to_string(FILE_PATH).unwrap();

    let hand_rankings: Vec<Hand> = Vec::new();

    for line in contents.lines()
    {
        let hand_and_bid: Vec<&str> = line.split(" ").collect();

        let hand = hand_and_bid[0];
        let bid: i32 = hand_and_bid[1].parse().unwrap();


    }

}
