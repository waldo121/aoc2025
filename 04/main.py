from typing import List, Tuple, Any
puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    lines = file.readlines()
grid_size = len(lines)
grid = [[]for _ in range(grid_size)]
for index, line in enumerate(lines):
    grid[index] = line.rstrip()

def get_adjacent_cells(x,y) -> List[tuple[int, int]]:
    adjacents: List[tuple[int,int]] = []
    if x-1 >= 0 and y-1 >=0:
        adjacents.append((x-1,y-1))
    if x-1 >= 0 and y+1 < grid_size:
        adjacents.append((x-1, y+1))
    if x+1 < grid_size and y-1 >=0:
        adjacents.append((x+1,y-1))
    if x+1 < grid_size and y+1 < grid_size:
        adjacents.append((x+1, y+1))
    if y+1 < grid_size:
        adjacents.append((x, y+1))
    if y-1 >=0:
        adjacents.append((x, y-1))
    if x-1 >= 0:
        adjacents.append((x-1, y))
    if x+1 < grid_size:
        adjacents.append((x+1, y))
    return adjacents

#p1
accessible = 0
for index_x in range(grid_size):
    for index_y in range(grid_size): 
        if grid[index_x][index_y] == '.':
            continue
        #count accessible rolls
        adjacents = 0
        adjacent_cells = get_adjacent_cells(index_x,index_y)
        for cell in adjacent_cells:
            if grid[cell[0]][cell[1]] == '@':
                adjacents += 1
        if adjacents < 4:
            accessible += 1
print("accessible: ", accessible)
#p2
def find_rolls(grid, grid_size) -> List[tuple[int,int]]:
    rolls = []
    for index_x in range(grid_size):
        for index_y in range(grid_size):
            if grid[index_x][index_y] == '@':
                rolls.append((index_x, index_y))
    return rolls

def get_removable_cells(rolls: List[tuple[int,int]], removed_cells: List[tuple[int,int]] = []) -> List[tuple[int,int]]:
    removable: List[tuple[int,int]] = []
    for roll_position in rolls:
        index_x,index_y = roll_position[0], roll_position[1]
        if grid[index_x][index_y] == '.' or (index_x,index_y) in removed_cells:
            continue
        #count accessible rolls
        adjacents = 0
        adjacent_cells = get_adjacent_cells(index_x,index_y)
        for cell in adjacent_cells:
            if grid[cell[0]][cell[1]] == '@' and not cell in removed_cells:
                adjacents += 1
        if adjacents < 4:
            removable.append((index_x, index_y))
    return removable
rolls = find_rolls(grid=grid, grid_size=grid_size)
removable_cells = get_removable_cells(rolls=rolls)
removed_cells = []

while len(removable_cells) != 0:
    removed_cells += removable_cells
    removable_cells = get_removable_cells(rolls=rolls, removed_cells=removed_cells)
print("removed :", len(removed_cells))
# note: I don't know for sure how long it took, but around 10-15min max, solution might be further optimisable