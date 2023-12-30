INPUT = [line.strip() for line in open('input/5.txt').readlines()]

def main() -> None:
    seeds = [int(x) for x in INPUT[0].replace("seeds: ", "").split(" ")]
    maps = [
        [[int(y) for y in x.split(" ")] for x in INPUT[i][1::]]
        for i in range(1, 8)
    ]
    print(maps)

if __name__ == "__main__":
    main()
