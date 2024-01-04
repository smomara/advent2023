from typing import List
from itertools import combinations

INPUT = [line.strip() for line in open('input/11.txt').readlines()]

class Map:
    def __init__(self):
        self.lines: List[str] = []
        self.galaxies: List[List[int]] = self._find_galaxies()

    def _find_galaxies(self) -> List[List[int]]:
        return [[x, y] for y, row in enumerate(self.lines) for x, c in enumerate(row) if c != '.']
    
    @classmethod
    def expand_galaxy(cls, lines: List[str], years: int) -> "Map":
        map = cls()
        map.lines = lines
        map.galaxies = map._find_galaxies()

        years -=1

        rows, cols = len(map.lines), len(map.lines[0])
        row_expansion = [0] * rows
        col_expansion = [0] * cols

        for y in range(rows):
            row_expansion[y] = row_expansion[y-1] + (years if set(lines[y]) == {'.'} else 0)
        for x in range(cols):
            col_expansion[x] = col_expansion[x-1] + (years if all(lines[y][x] == '.' for y in range(rows)) else 0)
        
        for galaxy in map.galaxies:
            galaxy[0] += col_expansion[galaxy[0]]
            galaxy[1] += row_expansion[galaxy[1]]

        return map

def eval(map: Map) -> int:
    return sum(abs(x[0] - y[0]) + abs(x[1] - y[1]) for x, y in combinations(map.galaxies, 2))

def part1(lines: List[str]) -> int:
    map = Map().expand_galaxy(lines, 2)
    return eval(map)

def part2(lines: List[str]) -> int:
    map = Map().expand_galaxy(lines, 1000000)
    return eval(map)

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()