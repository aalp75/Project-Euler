import numpy as np

# input
N = 10 # floor
global_size = 32 # width

all_lines = []

# generate all possible combination
def generate_line(curr_row, curr_size):
    if curr_size > global_size:
        return

    if curr_size + 2 == global_size or curr_size + 3 == global_size:
        all_lines.append(curr_row)
        return
    
    if curr_size == 0:
        last_pos = 0
    else:
        last_pos = curr_row[-1]

    for v in [2, 3]: 
        generate_line(curr_row + [curr_size + v], curr_size + v)

_ = generate_line([], 0)

lines = len(all_lines)
compatible = []

# check the compatibility
for i in range(lines):
    curr_compatible = []
    for j in range(lines):
        if np.intersect1d(all_lines[i], all_lines[j]).size == 0:
            curr_compatible.append(j)
        else:
            pass
    compatible.append(curr_compatible)

# count the solution using dynamic programming
dp = np.zeros((N + 1, lines), dtype='int')
dp[1] = np.ones(lines, dtype='int')

for i in range(2, N + 1):
    for j in range(lines):
        for k in compatible[j]:
            dp[i, j] += dp[i - 1, k]

res = dp[N].sum()

print("Solution: %d" %(res))