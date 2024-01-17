INPUT = [line.strip() for line in open('input/17.txt').readlines()]

def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def get_neighbors(lines, pos):
    neighbors = {}
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for d in directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos[0] in range(len(lines[0])) and new_pos[1] in range(len(lines)):
            neighbors[new_pos] = int(lines[new_pos[1]][new_pos[0]])
    return neighbors

def djikstra(lines):
    graph = {}
    for y, line in enumerate(lines):
        for x in range(len(line)):
            graph[(x, y)] = get_neighbors(lines, (x, y))

    costs = {}
    for node in graph.keys():
        costs[node] = float('inf')
    costs[(0, 0)] = 0

    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    print(costs[(len(lines)-1, len(lines)-1)])

def part1(lines: list[str]) -> int:
    djikstra(lines)
    return 0

def part2(lines: list[str]) -> int:
    return 0

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()