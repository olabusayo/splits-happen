import argparse

total_score = 0


def get_value(ind, bowling_line):
    char = bowling_line[ind]
    if char == "X":
        return 10
    elif char == "/":
        return 10 - int(bowling_line[ind-1])
    elif char == "-":
        return 0
    else:
        return int(char)


def handle_strike(ind, bowling_line):
    global total_score

    total_score += 10
    bonus_score = handle_bonus(ind, bowling_line, 2)
    total_score += bonus_score

def handle_spare(ind, bowling_line):
    global total_score

    total_score += get_value(ind, bowling_line)
    bonus_score = handle_bonus(ind, bowling_line, 1)
    total_score += bonus_score


def handle_miss(ind, bowling_line):
    pass # do nothing


def handle_reg(ind, bowling_line):
    global total_score

    total_score += get_value(ind, bowling_line)


def handle_bonus(ind, bowling_line, bonus_turns):
    score = 0
    for i in range(1, bonus_turns+1):
        new_ind = ind + i
        if new_ind < len(bowling_line):
            score += get_value(new_ind, bowling_line)
    return score


def process_input(bowling_line):
    # bowling_line = "5/5/5/5/5/5/5/5/5/5/5"
    # bowling_line = "9-9-9-9-9-9-9-9-9-9-"
    bowling_line = "X7/9-X-88/-6XXX81"

    frame_max = 10
    curr_turn = 0
    curr_frame = 0
    for ind in range(len(bowling_line)):
        curr_turn += 1
        curr_frame = curr_frame + 1 if curr_turn != 2 else curr_frame
        char = bowling_line[ind]
        if curr_frame <= frame_max:
            if char == "X":
                handle_strike(ind, bowling_line)
                curr_turn = 0
            elif char == '/':
                handle_spare(ind, bowling_line)
                curr_turn = 0
            elif char == '-':
                handle_miss(ind, bowling_line)
                if curr_turn == 2:
                    curr_turn = 0
            else:
                handle_reg(ind, bowling_line)
                if curr_turn == 2:
                    curr_turn = 0
    pass



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Valid sequence of rolls for one line of American Ten-Pin Bowling, "
                                      "where 'X' indicates a strike, '/' indicates a spare, '-' indicates a miss")
    args = parser.parse_args()
    print(args.input)
    process_input(args.input)
    pass


if __name__ == "__main__":
    main()

