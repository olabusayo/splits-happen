from ten_pin import *

sample_bls = {"8-7-539/9/X8-513/9-": 122, "8/9-44729-XX8-359/7": 133, "8-5/358171X9/XX8/6": 150,
              "X7/9-X-88/-6XXX81": 167, "35X3/81XX62547/X63": 155, "24X3/4-72-481--9/71": 91,
              "X1763X2/43452--927": 105, "237/428-812518444-9/7": 87, "X-/1318262532248/12": 84,
              "X9/61154/31623/5453": 106, "256-45-79/9-X115324": 85, "5/5/5/5/5/5/5/5/5/5/5": 150,
              "9-9-9-9-9-9-9-9-9-9-": 90, "X7/9-X-88/-6XXX81": 167, "XXXXXXXXXXXX": 300}
sample_bls_list = list(sample_bls)


def test_convert_turn_to_score():
    bl = sample_bls_list[0]  # ["8-7-539/9/X8-513/9-"]
    assert convert_turn_to_score(3, bl) == 0  # testing miss
    assert convert_turn_to_score(0, bl) == 8  # testing number
    assert convert_turn_to_score(10, bl) == 10  # testing strike
    assert convert_turn_to_score(7, bl) == 1  # testing spare
    assert convert_turn_to_score(8, bl) == 9  # testing number


def test_get_bonus_score():
    bl = sample_bls_list[8]  # ["X-/1318262532248/12"]
    assert get_bonus_score(0, bl) == 10
    assert get_bonus_score(2, bl) == 1
    assert get_bonus_score(16, bl) == 1
    bl = sample_bls_list[3]  # ["X7/9-X-88/-6XXX81"]
    assert get_bonus_score(0, bl) == 10
    assert get_bonus_score(2, bl) == 9
    assert get_bonus_score(9, bl) == 0
    bl = sample_bls_list[1]  # ["8/9-44729-XX8-359/7"]
    assert get_bonus_score(0, bl) == 0
    assert get_bonus_score(2, bl) == 0
    assert get_bonus_score(9, bl) == 0
    assert get_bonus_score(10, bl) == 18
    bl = sample_bls_list[6]  # ["X1763X2/43452--927"]
    assert get_bonus_score(2, bl) == 0
    assert get_bonus_score(7, bl) == 4
    assert get_bonus_score(9, bl) == 0
    bl = sample_bls_list[7]  # ["237/428-812518444-9/7"]
    assert get_bonus_score(0, bl) == 0
    assert get_bonus_score(2, bl) == 0
    assert get_bonus_score(7, bl) == 0


def test_get_turn_score_and_bonus():
    bl = sample_bls_list[8]  # ["X-/1318262532248/12"]
    assert convert_turn_to_score(0, bl) + get_bonus_score(0, bl) == 20
    bl = sample_bls_list[3]  # ["X7/9-X-88/-6XXX81"]
    assert convert_turn_to_score(0, bl) + get_bonus_score(0, bl) == 20
    assert convert_turn_to_score(5, bl) + get_bonus_score(5, bl) == 18
    assert convert_turn_to_score(12, bl) + get_bonus_score(12, bl) == 30
    assert convert_turn_to_score(13, bl) + get_bonus_score(13, bl) == 28
    assert convert_turn_to_score(14, bl) + get_bonus_score(14, bl) == 19
    bl = sample_bls_list[2]  # ["8-5/358171X9/XX8/6"]
    assert convert_turn_to_score(3, bl) + get_bonus_score(3, bl) == 8
    assert convert_turn_to_score(12, bl) + get_bonus_score(12, bl) == 11
    assert convert_turn_to_score(16, bl) + get_bonus_score(16, bl) == 8
    bl = sample_bls_list[3]  # ["X7/9-X-88/-6XXX81"]
    assert convert_turn_to_score(2, bl) + get_bonus_score(2, bl) == 12
    assert convert_turn_to_score(9, bl) + get_bonus_score(9, bl) == 2
    bl = sample_bls_list[4]  # [35X3/81XX62547/X63"]
    assert convert_turn_to_score(4, bl) + get_bonus_score(4, bl) == 15
    assert convert_turn_to_score(14, bl) + get_bonus_score(14, bl) == 13
    bl = sample_bls_list[2]  # ["8-5/358171X9/XX8/6"]
    assert convert_turn_to_score(8, bl) + get_bonus_score(8, bl) == 7
    assert convert_turn_to_score(15, bl) + get_bonus_score(15, bl) == 8
    bl = sample_bls_list[5]  # ["24X3/4-72-481--9/71"]
    assert convert_turn_to_score(3, bl) + get_bonus_score(3, bl) == 3
    assert convert_turn_to_score(11, bl) + get_bonus_score(11, bl) == 8
    bl = sample_bls_list[8]  # ["X-/1318262532248/12"]
    assert convert_turn_to_score(1, bl) + get_bonus_score(1, bl) == 0
    bl = sample_bls_list[3]  # [["X7/9-X-88/-6XXX81"]
    assert convert_turn_to_score(4, bl) + get_bonus_score(4, bl) == 0
    assert convert_turn_to_score(6, bl) + get_bonus_score(6, bl) == 0
    assert convert_turn_to_score(10, bl) + get_bonus_score(10, bl) == 0


def test_process_bowling_line():
    for bl in sample_bls:
        assert process_bowling_line(bl) == sample_bls[bl]

