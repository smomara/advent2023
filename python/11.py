from typing import List, Tuple

INPUT = [line.strip() for line in open('input/11.txt').readlines()]

class Map:
    def __init__(self, lines: List[str]):
        self.lines: List[str] = lines
        self.galaxies: List[Tuple[int, int]] = self._find_galaxies()

    def _find_galaxies(self) -> List[Tuple[int, int]]:
        return [(x, y) for x, row in enumerate(self.lines) for y, c in enumerate(row) if c != '.']

    # TODO optimize for large numbers
    def expand_galaxy(self, years: int) -> None:
        # identify and expand rows
        expanded_lines = []
        for y, row in enumerate(self.lines):
            if "#" not in row:
                expanded_lines.extend(['.' * len(row)] * years)
            expanded_lines.append(row)
        self.lines = expanded_lines
        
        # identify columns
        row_length = len(self.lines[0])
        columns_to_expand = [True] * row_length

        for row in self.lines:
            for x, c in enumerate(row):
                if c == '#':
                    columns_to_expand[x] = False
                    continue

        # expand identified columns
        for y in range(len(self.lines)):
            self.lines[y] = ''.join([c + ('.' * years if columns_to_expand[x] else '') for x, c in enumerate(self.lines[y])])
        
        # update galaxy location
        self.galaxies = self._find_galaxies()

def eval(map: Map) -> int:
    total = 0
    for i in range(len(map.galaxies)-1):
        for j in range(i+1, len(map.galaxies)):
            dist = abs(map.galaxies[i][0] - map.galaxies[j][0]) + abs(map.galaxies[i][1] - map.galaxies[j][1])
            total += dist
    return total

def part1(lines: List[str]) -> int:
    map = Map(lines)
    map.expand_galaxy(1)
    return eval(map)


def part2(lines: List[str]) -> int:
    map = Map(lines)
    map.expand_galaxy(1000000)
    return eval(map)

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    #print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()