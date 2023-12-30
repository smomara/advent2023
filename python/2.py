COLOR_LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def parse_line(line: str):
    game_r = line.find(":") - 1
    game_l = line.find(" ") + 1
    game_num = int(line[game_l:game_r + 1])

    handfuls = line[game_r + 3:].split("; ")
    proc_handfuls = []

    for handful in handfuls:
        handful = handful.split(" ")
        handful = [(int(value), color.strip(',').strip('\n')) for value, color in zip(handful[0::2], handful[1::2])]
        proc_handfuls.append(handful)

    return game_num, proc_handfuls

def is_game_valid(handfuls):
    for handful in handfuls:
        for value, color in handful:
            if value > COLOR_LIMITS[color]:
                return False
    return True

input_file = 'input/2.txt'
    
with open(input_file) as f:
    data = f.readlines()

total_score = 0

for line in data:
    game_num, handfuls = parse_line(line)
    total_score += game_num if is_game_valid(handfuls) else 0

print(total_score)
