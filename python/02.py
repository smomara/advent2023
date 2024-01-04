import re
from collections import Counter

INPUT = [line.strip() for line in open('input/02.txt').readlines()]

def parse_grab(grab: str) -> tuple[int, int, int]:
    counts: Counter[str] = Counter()
    for count_color in grab.split(", "):
        count, color = count_color.split()
        counts[color] = int(count)
    return counts["red"], counts["green"], counts["blue"]

def parse_line(line: str) -> tuple[int, tuple[tuple[int, int, int], ...]]:
    m = re.search(r"^Game (\d+): (.*)", line)
    assert m, line
    game_number, grabs = m.groups()

    return int(game_number), tuple(parse_grab(g) for g in grabs.split("; "))

def parse_line_1(line: str) -> int:
    game_number, grabs = parse_line(line)

    for r, g, b in grabs:
        if r > 12 or g > 13 or b > 14:
            return 0
    return game_number

def parse_line_2(line: str) -> int:
    game_number, grabs = parse_line(line)

    max_r, max_g, max_b = 0, 0, 0
    for r, g, b in grabs:
        max_r = max(max_r, r)
        max_g = max(max_g, g)
        max_b = max(max_b, b)
    
    return max_r * max_g * max_b

def part1(lines: list[str]) -> int:
    return sum(parse_line_1(line) for line in lines)

def part2(lines: list[str]) -> int:
    return sum(parse_line_2(line) for line in lines)

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()