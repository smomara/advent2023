INPUT = open('input/15.txt').read()

def parse1(line: str) -> list[str]:
    return line.split(',')

def parse2(line: str):
    return [[step.split("-")[0], step.split("-")[1]] if "-" in step else [step.split("=")[0], int(step.split("=")[1])] for step in parse1(line)]

def hash(string: str) -> int:
    acc = 0
    for c in string:
        acc = (acc + ord(c)) * 17 % 256
    return acc

def get_boxes(steps: list[str]) -> int:
    boxes = {i: [] for i in range(256)}

    for step in steps:
        key = hash(step[0])
        match = next((t for t in boxes[key] if t[0] == step[0]), None)

        if step[1]:
            if match:
                match[1] = step[1]
            else:
                boxes[key].append(step)
        else:
            if match:
                boxes[key].remove(match)
    
    return boxes

def part1(line: str) -> int:
    return sum(hash(step) for step in parse1(line))

def part2(line: str) -> int:
    return sum((k+1) * (i+1) * int(l[1]) for k, v in get_boxes(parse2(line)).items() for i, l in enumerate(v))

def main() -> None:
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")

if __name__ == "__main__":
    main()