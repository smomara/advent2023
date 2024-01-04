import re
from dataclasses import dataclass

INPUT = [line.strip() for line in open('input/05.txt').readlines()]

@dataclass(frozen=True)
class Range:
    dst: int
    src: int
    length: int

    def __contains__(self, seed: int) -> bool:
        return self.src <= seed < self.src + self.length

    def __getitem__(self, seed: int) -> int:
        return self.dst + (seed - self.src)

class Solver:
    def __init__(self, debug=False):
        self.seeds: list[int] = []
        self.maps: dict[str, list[Range]] = {}
        if debug:
            self.debug = print
        else:
            self.debug = lambda *args, **kwargs: None

    @classmethod
    def parse(cls, lines: list[str], debug=False) -> "Solver":
        solver = cls(debug)
        m = re.search(r"^seeds: (.*)", lines[0])
        assert m
        solver.seeds.extend(map(int, m.group(1).split()))
        map_name = None
        for line in lines[1:]:
            if m := re.search(r"^(.*) map:", line):
                map_name = m.group(1)
                continue
            if not map_name:
                continue
            if m := re.search(r"^\d", line):
                ranges = solver.maps.setdefault(map_name, [])
                ranges.append(Range(*map(int, line.split())))
        return solver

    def find_location(self, seed: int) -> int:
        for name, ranges in self.maps.items():
            for r in ranges:
                if seed in r:
                    seed = r[seed]
                    break
        return seed
    
    def find_min_location_range(self, start: int, length: int) -> int:
        if length == 1:
            return min(self.find_location(start), self.find_location(start + 1))

        step_size = length // 2
        middle = start + step_size

        start_loc = self.find_location(start)
        middle_loc = self.find_location(middle)
        end_loc = self.find_location(start + length)
        found_min = float('inf')

        if start_loc + step_size != middle_loc:
            found_min = self.find_min_location_range(start, step_size)
        if middle_loc + (length - step_size) != end_loc:
            found_min = min(found_min, self.find_min_location_range(middle, length - step_size))

        return found_min

def part1(solver: Solver) -> int:
    return min(solver.find_location(seed) for seed in solver.seeds)

def part2(solver: Solver) -> int:
    return min([solver.find_min_location_range(start, length) for start, length in zip(solver.seeds[::2], solver.seeds[1::2])])

def main() -> None:
    solver = Solver.parse(INPUT)
    print(f"Part 1: {part1(solver)}")
    print(f"Part 2: {part2(solver)}")

if __name__ == "__main__":
    main()
