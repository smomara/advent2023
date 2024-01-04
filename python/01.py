import re

INPUT = [line.strip() for line in open('input/01.txt').readlines()]

def parse1(line: str) -> int:
    m = re.search(r"(\d)", line)
    assert m, line
    x = m.group(1)

    m = re.search(r".*(\d)", line)
    assert m, line
    y = m.group(1)

    return int(f"{x}{y}")

def parse2(line: str) -> int:
    words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pattern = r"(\d|" + "|".join(words) + ")"
    m = re.search(pattern, line)
    assert m, line
    x = words.get(m.group(1), m.group(1))

    m = re.search(f".*{pattern}", line)
    assert m, line
    y = words.get(m.group(1), m.group(1))

    return int(f"{x}{y}")

def part1(lines: list[str]) -> int:
    return sum(parse1(line) for line in lines)

def part2(lines: list[str]) -> int:
    return sum(parse2(line) for line in lines)

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()