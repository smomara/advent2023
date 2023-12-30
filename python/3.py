import re
import itertools
from dataclasses import dataclass
from typing import Iterator

INPUT = [line.strip() for line in open('input/3.txt').readlines()]

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

def main() -> None:
    graph = Graph.parse(INPUT)
    print(part1(graph))

if __name__ == "__main__":
    main()