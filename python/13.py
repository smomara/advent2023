from typing import List

INPUT = [line.strip() for line in open('input/13.txt').readlines()]

def is_symmetric(lines, y, is_part_2=False):
    top = y-1
    bottom = y

    smudge_fixed = not is_part_2
    while top >= 0 and bottom < len(lines):
        if sum(t != b for t, b in zip(lines[top], lines[bottom])) == 1 and not smudge_fixed:
            smudge_fixed = True
        elif lines[top] != lines[bottom]:
            return False
        top -= 1
        bottom += 1

    return smudge_fixed

def eval(pattern: List[str], is_part_2=False):
    for y in range(1, len(pattern)):
        if is_symmetric(pattern, y, is_part_2):
            return y * 100
    
    rotated = list(zip(*reversed(pattern)))
    for x in range(1, len(rotated)):
        if is_symmetric(rotated, x, is_part_2):
            return x
        
    return 0
        
def parse(lines: List[str]) -> List[List[str]]:
    patterns = []
    prev = 0
    for i, line in enumerate(lines):
        if line == '':
            patterns.append(lines[prev:i])
            prev = i+1
    patterns.append(lines[prev:i])
    return patterns

def part1(lines: List[str]) -> int:
    return sum(eval(pattern) for pattern in parse(lines))

def part2(lines: List[str]) -> int:
    return sum(eval(pattern, True) for pattern in parse(lines))

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()