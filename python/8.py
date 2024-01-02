from typing import Dict, Tuple, List, Set
from itertools import cycle
import numpy as np
import re

INPUT = [line.strip() for line in open('input/8.txt').readlines()]

class Graph:
    def __init__(self) -> None:
        self.nodes: Dict[str, Tuple[str]] = {}
        self.instructions: List[int] = []
        self.starting: List[str] = []
        self.ending: Set[str] = set()
    
    @classmethod
    def parse(cls, lines: List[str]) -> "Graph":
        graph = cls()

        graph.instructions = [1 if c == 'R' else 0 for c in lines[0]]

        pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')
        for line in lines[2:]:
            match = pattern.search(line)
            parent = match.group(1)
            children = (match.group(2), match.group(3))
            graph.nodes[parent] = children

            if parent[2] == 'A':
                graph.starting.append(parent)

            if parent[2] == 'Z':
                graph.ending.add(parent)

        return graph
    
    def steps1(self, root: str, ending: Set[str]) -> int:
        steps = 0
        instructions_iter = cycle(self.instructions)

        while root not in ending:
            instruction = next(instructions_iter)
            root = self.nodes[root][instruction]
            steps += 1
        return steps
    
    def steps2(self):
        steps = []

        for root in self.starting:
            steps.append(self.steps1(root, self.ending))
            
        return np.lcm.reduce(steps)


def part1(graph: Graph) -> int:
    return graph.steps1('AAA', set(['ZZZ']))

def part2(graph: Graph) -> int:
    return graph.steps2()

def main() -> None:
    graph = Graph.parse(INPUT)
    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")

if __name__ == "__main__":
    main()