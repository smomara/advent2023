from collections import Counter
import re

INPUT = [line.strip() for line in open('input/4.txt').readlines()]

def parse_line(line: str) -> tuple[int, set[int], set[int]]:
    m = re.search(r"^Card\s+(\d+):\s+(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)", line)
    assert m, line
    card_number, winners, havers = m.groups()
    return int(card_number), set([num for num in winners.split()]), set([num for num in havers.split()])

def num_matches(line: str) -> int:
    _, win, have = parse_line(line)
    return len(win & have)

def eval1(line: str) -> int:
    num_win = num_matches(line)
    return 2 ** (num_win - 1) if num_win else 0

def part1(lines: list[str]) -> int:
    return sum(map(eval1, lines))

def part2(lines: list[str]) -> int:
    num_lines = len(lines)
    copies: Counter[int] = Counter(range(1, num_lines+1))

    for i, line in enumerate(lines, 1):
        num_wins = num_matches(line)
        for j in range(i + 1, min(i + 1 + num_wins, num_lines + 1)):
            copies[j] += copies[i]
    
    return sum(copies.values())

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()