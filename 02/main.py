import sys
from itertools import repeat

puzzle_input = "input.txt"
lines = []
with open(puzzle_input, "r") as file:
    line = file.readline()

#p1
ranges = line.split(",") 
sum_invalid = 0
def is_id_invalid_p1(id: str) -> bool:
    size = len(id)
    return id[0:size//2] == id[size//2:]

#p2
def is_id_invalid_p2(id: str) -> bool:
    id_size = len(id)
    for i in range(1,id_size//2+1):
        pattern_size = len(id[0:i])
        if "".join(repeat(id[0:i],id_size//pattern_size)) == id:
            return True
    return False

for r in ranges:
    numbers = r.split("-")
    for n in range(int(numbers[0]), int(numbers[1])+1):
        if is_id_invalid_p2(str(n)):
            sum_invalid += n
print(sum_invalid)