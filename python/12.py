from typing import Tuple, List
from itertools import product

INPUT = 'input/12.txt'

def read_input(file_path: str) -> List[str]:
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]

def parse(line: str) -> Tuple[str, Tuple[int, ...]]:
    pattern, groups = line.split()
    return pattern, tuple(map(int, groups.split(',')))

def count_arrangements(pattern: str, group_sizes: Tuple[int, ...]) -> int:
    pattern = [None if x == '?' else x == '.' for x in pattern]
    possibilities = product([True, False], repeat=pattern.count(None))

    valid_count = 0
    for possibility in possibilities:
        temp_pattern = pattern.copy()
        pos_index = 0
        for i in range(len(pattern)):
            if temp_pattern[i] is None:
                temp_pattern[i] = possibility[pos_index]
                pos_index += 1
        if is_valid_pattern(temp_pattern, group_sizes):
            valid_count += 1
    return valid_count

def is_valid_pattern(pattern, group_sizes):
    current_group_size = 0
    for size in group_sizes:
        found = False
        while current_group_size < len(pattern):
            if pattern[current_group_size]:
                if found:
                    break
                current_group_size += 1
                continue
            count = 0
            while current_group_size < len(pattern) and not pattern[current_group_size]:
                count += 1
                current_group_size += 1
            if count == size:
                found = True
                break
            else:
                return False
        if not found:
            return False
    return all(pattern[current_group_size:])

def part1(lines: list[str]) -> int:
    return sum(count_arrangements(*parse(line)) for line in lines)

def part2(lines: list[str]) -> int:
    return 0

def main() -> None:
    input = read_input(INPUT)
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")

if __name__ == "__main__":
    main()