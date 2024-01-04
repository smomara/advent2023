from typing import List

INPUT = [line.strip() for line in open('input/9.txt').readlines()]

def parse(lines: List[str]) -> List[List[int]]:
        return [[[int(x) for x in line.split(" ")]] for line in lines]

def eval(history: List[int]) -> int:
    while sum(history[-1]) != 0:
        history.append([r - l for l, r in zip(history[-1], history[-1][1:])])
    return sum([line[-1] for line in history])

def part1(histories: List[List[int]]) -> int:
    return sum([eval(history) for history in histories])

def part2(lines: List[str]) -> int:
    return 0

def main() -> None:
    histories = parse(INPUT)
    print(f"Part 1: {part1(histories)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()