import sys
from collections import deque
import math

puzzle_input = "input.txt"
count = 0
dial_numbers = deque([i for i in range(100)])
dial_numbers.rotate(50)
lines = []
with open(puzzle_input, "r") as file:
    lines = file.readlines()
#p1
for l in lines:
    direction = l[0]
    positions = int(l[1:])
    rotation = 0
    if direction == "R":
        rotation = positions
    elif direction == "L":
        rotation = positions * -1
    dial_numbers.rotate(rotation)
    # count number of times dial is 0
    if dial_numbers[0] == 0:
        count += 1
print("Password: ", count)
#p2
for l in lines:
    direction = l[0]
    positions = int(l[1:])
    rotation = 0
    current_position = dial_numbers[0]
    way_to_turn = 1
    if direction == "R":
        way_to_turn = -1
    elif direction == "L":
        way_to_turn = 1
    # count extra clicks through rotation
    # rotate one position at a time
    for i in range(positions):
        dial_numbers.rotate(way_to_turn)
        # count number of times dial is 0
        if dial_numbers[0] == 0:
            count += 1
print("Password: ", count)