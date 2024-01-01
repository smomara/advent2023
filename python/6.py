from typing import Dict, List
from functools import reduce

INPUT = [line.strip() for line in open('input/6.txt').readlines()]

def eval(time: int, distance: int) -> int:
    # TODO: improve speed, implement binary search
    x = 0
    while x * (time - x) <= distance:
        x += 1
    min_val = x

    while x * (time - x) > distance:
        x += 1
    max_val = x

    return max_val - min_val

def parse1(lines: List[str]) -> Dict[int, Dict[str, int]]:
    result_dict = {}

    for line in lines:
        key, values = line.split(":")
        key = key.strip().lower()
        values = [int(val) for val in values.split()]

        for i, val in enumerate(values):
            if i + 1 not in result_dict:
                result_dict[i + 1] = {}
            result_dict[i+1][key] = val

    return result_dict

def parse2(lines: List[str]) -> Dict[str, int]:
    result_dict = {}

    for line in lines:
        key, values = line.split(":")
        key = key.strip().lower()
        value = int(''.join(values.split()))
        result_dict[key] = value

    return result_dict

def part1(lines: List[str]) -> int:
    return reduce(lambda x, y: x * y, (eval(**info) for info in parse1(lines).values()), 1)

def part2(lines: List[str]) -> int:
    return eval(**parse2(lines))

def main() -> None:
    print(part1(INPUT))
    print(part2(INPUT))

if __name__ == "__main__":
    main()
