from enum import IntEnum

INPUT_FILE = "input.text"

possible_letter_cards = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 11,
    "T" : 10
}

class HandType(IntEnum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1

def card_to_value(card : str) -> int | None:
    if len(card) > 1:
        print("Input is more than one character")
        return None

    if card in possible_letter_cards:
        return possible_letter_cards[card]

    elif card.isdigit():
        num = int(card)
        if num <= 9 and num >= 2:
            return num
        else:
            print(f"Card invalid, Card: {card}")
            return None

class Hand:
    cards : str
    card_values : list[int]
    bid : int
    hand_type : HandType

    def __init__(self, hand : str, bid : int):
        self.bid = bid

        self.cards = hand
        self.card_values = []
        self.find_hand_type()
        self.get_card_values()
        print(f"Found hand type is {self.hand_type}")
        print(f"Card Values: {self.card_values}")

    def find_hand_type(self) -> None:

        matches : list[int] = []
        print(f"Cards: {self.cards}")
        for card in self.cards:
            temp_cards = self.cards

            temp_cards = temp_cards.replace(card, "")

            matches.append(len(temp_cards))

        print(f"Matches: {matches}")

        if matches.count(0) == 5:
            self.hand_type = HandType.FiveOfAKind
        elif matches.count(1) == 4:
            self.hand_type = HandType.FourOfAKind
        elif matches.count(2) == 3 and matches.count(3) == 2:
            self.hand_type = HandType.FullHouse
        elif matches.count(2) == 3:
            self.hand_type = HandType.ThreeOfAKind
        elif matches.count(3) == 4:
            self.hand_type = HandType.TwoPair
        elif matches.count(3) == 2:
            self.hand_type = HandType.OnePair
        else:
            self.hand_type = HandType.HighCard

    def get_card_values(self) -> None:
        for card in self.cards:
            self.card_values.append(card_to_value(card))

def main() -> None:
    with open(INPUT_FILE, "r") as f:
        data = f.readlines()


    # Get all our hands and figure out what they ard
    hands: list[Hand] = []
    for line in data:
        hand, bid = line.split()

        hands.append(Hand(hand, int(bid)))


    # Sort and decide rank
    total = 0
    sorted_hands: list[Hand] = bubbleSortHands(hands)

    for i in range(0, len(sorted_hands)):
        rank = i + 1

        total += sorted_hands[i].bid * rank

    print(f"Total Winnings: {total}")

# is it fast? probably not, but it works
def bubbleSortHands(arr: list[Hand]) -> list[Hand]:
    n: int = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j].hand_type > arr[j + 1].hand_type:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            elif arr[j].hand_type == arr[j + 1].hand_type:
                for card_index in range(0, 5):
                    if arr[j].card_values[card_index] > arr[j + 1].card_values[card_index]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                        break
                    elif arr[j].card_values[card_index] < arr[j + 1].card_values[card_index]:
                        break


        if (swapped == False):
            break

    return arr


if __name__ == "__main__":
    main()
