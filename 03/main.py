import itertools
puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    lines = file.readlines()
#p1
sum = 0
for battery_bank in lines:
    batteries_combination = itertools.combinations(battery_bank.rstrip(),2)
    unique_batteries_combination = set(batteries_combination)
    max_joltage = max(map(lambda x: int("".join(x)), unique_batteries_combination))
    sum += max_joltage        
print("joltage_sum p1: ", sum)
#p2
def max_joltage_p2(bank: str) -> int:
    def bank_indexes(string: str, start: int = 0):
        # produce {[1]: [0,1,3]
        # [2]: [2,4,5]}
        # output
        position_map = {}
        for position, joltage in enumerate(bank[start:], start=start):
            try:
                position_map[int(joltage)].append(position)
            except KeyError:
                position_map[int(joltage)] = [position]
        return position_map
    def build_max(bank, bank_length: int, last_char_index: int = -1, current: str = "", target_length: int = 12) -> int:
        # bank : batteries available
        # bank_length : how long is the battery bank
        # last_char_index : from where in the bank can we pick characters to add
        # current : current maximum jotlage combination
        # target_length : how long the battery combination must be
        # recursive
        # exit condition
        if len(current) == target_length:
            return int(current)
        position_map = bank_indexes(bank, last_char_index + 1)
        remaining_characters_to_add = target_length-len(current)
        # find valid max number we can use
        max_joltage = max(position_map.keys())
        max_joltage_index = position_map[max_joltage][0]
        found_next_max = max_joltage_index > last_char_index and remaining_characters_to_add <= bank_length-max_joltage_index
        while not found_next_max:
            del position_map[max_joltage]
            max_joltage = max(position_map.keys())
            max_joltage_index = position_map[max_joltage][0]
            found_next_max = max_joltage_index > last_char_index and remaining_characters_to_add <= bank_length-max_joltage_index
        # use the max char
        current += str(max_joltage)
        return build_max(bank=bank, bank_length=bank_length, last_char_index=max_joltage_index, current=current, target_length=target_length)
    return build_max(bank=bank.rstrip(),bank_length=len(bank))
sum = 0
for battery_bank in lines:
    sum += max_joltage_p2(battery_bank.rstrip())        
print("joltage_sum p2: ", sum)
