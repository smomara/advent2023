from typing import List, Tuple, Dict
from queue import Queue

INPUT = [line.strip() for line in open('input/10.txt').readlines()]

MAP = {
    "|": [ ( 0,-1), ( 0, 1) ],
    "-": [ (-1, 0), ( 1, 0) ],
    "L": [ ( 0,-1), ( 1, 0) ],
    "J": [ ( 0,-1), (-1, 0) ],
    "7": [ (-1, 0), ( 0, 1) ],
    "F": [ ( 1, 0), ( 0, 1) ],
}

class Graph:
    def __init__(self, lines: List[str], map: Dict[str, List[Tuple[int, int]]]) -> None:
        self.lines = lines
        self.start = self._find_start()
        self.map = map
        self.dists = self._find_dists()
    
    def _find_start(self) -> Tuple[int, int]:
        return next(((xi, yi) for yi, line in enumerate(self.lines) 
                     for xi, c in enumerate(line) if c == "S"), (None, None))
    
    def _find_dists(self) -> Dict[Tuple[int, int], int]:
        q = Queue()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c = self.lines[self.start[1] + dy][self.start[0] + dx]
            if c in self.map:
                for dx2, dy2 in self.map[c]:
                    if self.start[0] == self.start[0] + dx + dx2 and self.start[1] == self.start[1] + dy + dy2:
                        q.put((1, (self.start[0] + dx, self.start[1] + dy)))

        dists = {self.start: 0}
        while not q.empty():
            d, (x, y) = q.get()
            if (x, y) in dists:
                continue
            dists[(x, y)] = d
            for dx, dy in self.map[self.lines[y][x]]:
                q.put((d + 1, (x + dx, y + dy)))
        
        return dists
                
    def furthest_point(self) -> int:
        return max(self.dists.values())
    
    def inside_count(self) -> int:
        w, h = len(self.lines[0]), len(self.lines)
        inside_count = 0
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if (x, y) in self.dists:
                    continue
                crosses = 0
                x2, y2 = x, y
                while x2 < w and y2 < h:
                    c2 = self.lines[y2][x2]
                    if (x2, y2) in self.dists and c2 != "L" and c2 != "7":
                        crosses += 1
                    x2 += 1
                    y2 += 1
                if crosses % 2 == 1:
                    inside_count += 1
        return inside_count

def part1(graph: Graph) -> int:
    return graph.furthest_point()

def part2(graph: Graph) -> int:
    return graph.inside_count()

def main() -> None:
    graph = Graph(INPUT, MAP)
    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")

if __name__ == "__main__":
    main()