# Inputs
# 1. Number of rows in patch
# 2. Number of cols in patch
# N. Row of patch e.g. S*SMSM (* = bail, s = small pumpkin, m = medium pumpkin, l = large pumpkin)
# 4. Farmer starting position (row)
# 5. Farmer starting position (col)

num_rows_in_patch = int(input())
num_cols_in_patch = int(input())
cell_map = {}
pumpkin_map = { 'S': 1, 'M': 5, 'L': 10 }
for i in range(num_rows_in_patch):
    cell_map[i] = str(input())

pos_row = int(input())
pos_col = int(input())

available = []

def check_around(pr, pc):
    if (pr < 0 or pr >= num_rows_in_patch) or (pc < 0 or pc >= num_cols_in_patch):
        return

    if cell_map[pr][pc] == "*":
        return
    elif [pr, pc] not in available:
        available.append([pr, pc])
        check_around(pr+1, pc)
        check_around(pr-1, pc)
        check_around(pr, pc+1)
        check_around(pr, pc-1)

check_around(pos_row, pos_col)
total_price = 0
for coord in available:
    price = pumpkin_map[cell_map[coord[0]][coord[1]]]
    total_price += price 

print(total_price)
