from collections import deque

INPUT = [line.strip() for line in open('input/16.txt').readlines()]

def count_energized_tiles(lines: list[str], starting_position=(-1, 0), debug=False) -> int:
    rows, cols = len(lines), len(lines[0])
    energized_tiles = set()
    traversed_path = set()

    map_energized = [''.join(['.' for _ in line]) for line in lines]

    if starting_position[0] == -1:
        starting_direction = (1, 0)
    elif starting_position[0] == rows:
        starting_direction = (-1, 0)
    elif starting_position[1] == -1:
        starting_direction = (0, 1)
    elif starting_position[1] == cols:
        starting_direction = (0, -1)

    queue = deque()
    queue.append((starting_position, starting_direction))

    while queue:
        position, direction = queue.popleft()

        #caching
        if (position, direction) in traversed_path:
            continue
        traversed_path.add((position, direction))

        #update position and check if in bounds
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if next_position[0] not in range(cols) or next_position[1] not in range(rows):
            continue

        #energize
        energized_tiles.add(next_position)
        tile = lines[next_position[1]][next_position[0]]

        #print
        if debug:
            map_energized[next_position[1]] = map_energized[next_position[1]][:next_position[0]] + "#" + map_energized[next_position[1]][next_position[0]+1:]
            for line in map_energized:
                print(line)
            print(lines[next_position[1]][next_position[0]], direction)
            print()

        # determine next steps
        if tile == '.':
            queue.append((next_position, direction))

        elif tile == '-':
            if direction[1] == 0:
                queue.append((next_position, direction))
            else:
                queue.append((next_position, (1, 0)))
                queue.append((next_position, (-1, 0)))

        elif tile == '|':
            if direction[0] == 0:
                queue.append((next_position, direction))
            else:
                queue.append((next_position, (0, 1)))
                queue.append((next_position, (0, -1)))

        elif tile == '\\':
            queue.append((next_position, (direction[1], direction[0])))

        elif tile == '/':
            queue.append((next_position, (-direction[1], -direction[0])))

    return len(energized_tiles)

def part1(lines: list[str]) -> int:
    return count_energized_tiles(lines)

def part2(lines: list[str]) -> int:
    height, width = len(lines), len(lines[0])
    positions = [(-1, i) for i in range(height)]
    positions += [(width, i) for i in range(height)]
    positions += [(i, -1) for i in range(width)]
    positions += [(i, height) for i in range(width)]
    return max(count_energized_tiles(lines, pos) for pos in positions)

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()