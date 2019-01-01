import argparse


def convert_turn_to_score(ind, bowling_line):
    char = bowling_line[ind]
    if char == "X":
        return 10
    elif char == "/":
        return 10 - convert_turn_to_score(ind - 1, bowling_line)
    elif char == "-":
        return 0
    else:
        return int(char)


def get_bonus_score(ind, bowling_line):
    score = 0
    bonus_turns = 0

    if bowling_line[ind] == "X":
        bonus_turns = 2
    elif bowling_line[ind] == "/":
        bonus_turns = 1

    for i in range(1, bonus_turns+1):
        new_ind = ind + i
        if new_ind < len(bowling_line):
            score += convert_turn_to_score(new_ind, bowling_line)
    return score


def process_bowling_line(bowling_line):
    total_score = 0
    frame_max = 10
    curr_turn = 0
    curr_frame = 0
    for ind in range(len(bowling_line)):
        curr_turn += 1
        curr_frame = curr_frame + 1 if curr_turn != 2 else curr_frame
        char = bowling_line[ind]
        if curr_frame <= frame_max:
            total_score += convert_turn_to_score(ind, bowling_line) + get_bonus_score(ind, bowling_line)
            if any(i == char for i in ("X", "/")):
                curr_turn = 0
            elif curr_turn == 2:
                curr_turn = 0
    return total_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Valid sequence of rolls for one line of American Ten-Pin Bowling, "
                                      "where 'X' indicates a strike, '/' indicates a spare, '-' indicates a miss")
    args = parser.parse_args()
    print(f"The total score for the bowling line '{args.input}' is {process_bowling_line(args.input.upper())}")


if __name__ == "__main__":
    main()

