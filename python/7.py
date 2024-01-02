from typing import List, Tuple

INPUT = [line.strip() for line in open('input/7.txt').readlines()]

class Hand:
    def __init__(self, cards: str):
        self.cards = cards.translate(str.maketrans('TJQKA', 'ABCDE'))

    @property
    def rank(self) -> int:
        return sum(map(self.cards.count, self.cards))

def parse1(line: str) -> int:
    hand, bid = line.split(" ")
    hand = Hand(hand)
    return hand.rank, hand.cards, int(bid)

def parse2(line: str) -> int:
    cards, bid = line.split(" ")

    frequencies = sorted(cards.replace("J", ""), key=lambda x: cards.count(x))
    top = "1" if len(frequencies) == 0 else frequencies[-1]
    rank = Hand(cards.replace("J", top)).rank
    cards = Hand(cards.replace("J", "0")).cards

    return rank, cards, int(bid)

def part1(lines: List[str]) -> int:
    return sum(
        (i+1) * v[2] for i, v in enumerate(
            sorted(
                [parse1(line) for line in lines],
                key=lambda x: (x[0], x[1])
            )
        )
    )

def part2(lines: List[str]) -> int:
    return sum(
        (i+1) * v[2] for i, v in enumerate(
            sorted(
                [parse2(line) for line in lines],
                key=lambda x: (x[0], x[1])
            )
        )
    )

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()