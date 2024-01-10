import time

INPUT = [line.strip() for line in open('input/14.txt').readlines()]

def slide(lines: list[str], direction: str = "north") -> list[str]:
    char_lines = [list(line) for line in lines]
    rows, cols = len(char_lines), len(char_lines[0])

    if direction == 'north':
        for y, char_line in enumerate(char_lines):
            for x, c in enumerate(char_line):
                if c == 'O' and y-1 >= 0 and char_lines[y-1][x] == '.':
                    i = 1
                    while y-i >= 0 and char_lines[y-i][x] == '.':
                        i += 1
                    char_lines[y][x], char_lines[y-i+1][x] = char_lines[y-i+1][x], char_lines[y][x]

    elif direction == 'south':
        for y in range(rows-1, -1, -1):
            char_line = char_lines[y]
            for x, c in enumerate(char_line):
                if c == 'O' and y+1 < rows and char_lines[y+1][x] == '.':
                    i = 1
                    while y+i < rows and char_lines[y+i][x] == '.':
                        i += 1
                    char_lines[y][x], char_lines[y+i-1][x] = char_lines[y+i-1][x], char_lines[y][x]

    elif direction == 'west':
        for y, char_line in enumerate(char_lines):
            for x, c in enumerate(char_line):
                if c == 'O' and x-1 >= 0 and char_lines[y][x-1] == '.':
                    i = 1
                    while x-i >= 0 and char_lines[y][x-i] == '.':
                        i += 1
                    char_lines[y][x], char_lines[y][x-i+1] = char_lines[y][x-i+1], char_lines[y][x]

    elif direction == 'east':
        for y, char_line in enumerate(char_lines):
            for x in range(cols-1, -1, -1):
                c = char_line[x]
                if c == 'O' and x+1 < cols and char_lines[y][x+1] == '.':
                    i = 1
                    while x+i < cols and char_lines[y][x+i] == '.':
                        i += 1
                    char_lines[y][x], char_lines[y][x+i-1] = char_lines[y][x+i-1], char_lines[y][x]

    return [''.join(char_line) for char_line in char_lines]

def cycle(lines: list[str], times: int) -> list[str]:
    seen_lines = {tuple(lines): 0}

    for i in range(1, times + 1):
        lines = slide(lines, 'north')
        lines = slide(lines, 'west')
        lines = slide(lines, 'south')
        lines = slide(lines, 'east')

        tuple_lines = tuple(lines)
        if tuple_lines in seen_lines:
            first_seen_i = seen_lines[tuple_lines]
            cycle_length = i - first_seen_i
            remaining_cycles = (times - i) % cycle_length
            return find_state_at_cycle(seen_lines, first_seen_i + remaining_cycles)
        else:
            seen_lines[tuple_lines] = i

    return lines

def find_state_at_cycle(seen_lines, cycle_index):
    for k, v in seen_lines.items():
        if v == cycle_index:
            return list(k)
    return None

def part1(lines: list[str]) -> int:
    return sum(len(lines)-y for y, line in enumerate(slide(lines)) for c in line if c == "O")

def part2(lines: list[str]) -> int:
    return sum(len(lines)-y for y, line in enumerate(cycle(lines, 1000000000)) for c in line if c == "O")

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()