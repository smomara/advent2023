from typing import List

INPUT = [line.strip() for line in open('input/9.txt').readlines()]

def parse(lines: List[str]) -> List[List[int]]:
        return [[[int(x) for x in line.split(" ")]] for line in lines]

def eval1(history: List[int]) -> int:
    while sum(history[-1]) != 0:
        history.append([r - l for l, r in zip(history[-1], history[-1][1:])])
    return sum([line[-1] for line in history])

def eval2(history: List[int]) -> int:
    # Generate new lines until all 0
    while sum(history[-1]) != 0:
        history.append([r - l for l, r in zip(history[-1], history[-1][1:])])
   
    # Reconstruct history in reverse
    for i in range(len(history) - 2, -1, -1):
        history[i].insert(0, history[i][0] - history[i+1][0])

    return history[0][0]

def part1(histories: List[List[int]]) -> int:
    return sum([eval1(history) for history in histories])

def part2(histories: List[List[int]]) -> int:
    return sum([eval2(history) for history in histories])

def main() -> None:
    histories = parse(INPUT)
    print(f"Part 1: {part1(histories)}")
    print(f"Part 2: {part2(histories)}")

if __name__ == "__main__":
    main()