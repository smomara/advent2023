import re
import itertools
from operator import mul
from dataclasses import dataclass
from typing import Iterator

INPUT = [line.strip() for line in open('input/03.txt').readlines()]

BORDER = list(
    complex(x, y) 
    for x, y in itertools.product(range(-1, 2), range(-1, 2))
    if (x, y) != (0, 0)
)

@dataclass(frozen=True)
class Part:
    pos: complex
    num: int

@dataclass(frozen=True)
class Symbol:
    pos: complex
    char: str

    @property
    def border(self) -> Iterator[complex]:
        for offset in BORDER:
            yield self.pos + offset

    @property
    def is_gear(self) -> bool:
        return self.char == "*"

    def intersect(self, coords: set[complex]) -> set[complex]:
        return set(self.border) & coords
    
class Graph:
    def __init__(self) -> None:
        self.parts: dict[complex, Part] = {}
        self.symbols: list[Symbol] = []

    @classmethod
    def parse(cls, lines) -> "Graph":
        graph = cls()
        for y, line in enumerate(lines):
            for m in re.finditer(r"\d+", line):
                pos = complex(m.start(), y)
                part = Part(pos, int(m.group()))
                for x in range(*m.span()):
                    graph.parts[complex(x, y)] = part
            for m in re.finditer(r"[^\d.]", line):
                pos = complex(m.start(), y)
                sym = Symbol(pos, m.group())
                graph.symbols.append(sym)
        
        return graph
    
    @property
    def gears(self) -> list[Symbol]:
        return [sym for sym in self.symbols if sym.is_gear and len(self.adjacent_parts(sym)) == 2]
    
    def adjacent_parts(self, symbol) -> list[Part]:
        parts = set()
        for pos in symbol.intersect(set(self.parts)):
            parts.add(self.parts[pos])
        return list(parts)
    
def part1(graph: Graph) -> int:
    total = 0
    for sym in graph.symbols:
        total += sum(p.num for p in graph.adjacent_parts(sym))
    return total

def part2(graph: Graph) -> int:
    total = 0
    for gear in graph.gears:
        part_nums = [p.num for p in graph.adjacent_parts(gear)]
        total += mul(*part_nums)
    return total

def main() -> None:
    graph = Graph.parse(INPUT)
    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")

if __name__ == "__main__":
    main()