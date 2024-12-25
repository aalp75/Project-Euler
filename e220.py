import time
import numpy as np
import math

LEFT_ROTATION = np.array([[0, -1], [1, 0]])
RIGHT_ROTATION = np.array([[0, 1], [-1, 0]])
POSITON_P2 = []

# precompute all position at a power of 2 numbers of step
def precompute_p2_position(n):
    curr_pos = np.array([0, 1])
    POSITON_P2.append(curr_pos)
    for i in range(n):
        move = RIGHT_ROTATION @ curr_pos
        curr_pos = curr_pos + move
        POSITON_P2.append(curr_pos)

# compute recursively the position after a given number of steps
def solve(steps):
    p2 = int(math.log2(steps))
    if (steps == 0):
        return np.array([0, 0])
    diff = steps - (1 << p2)
    adjustment = np.array([0, 0])
    if diff > 0:
        adjustment = POSITON_P2[p2] - solve((1 << p2) - diff)
    return POSITON_P2[p2] + RIGHT_ROTATION @ adjustment


def main():
    start = time.time()
    # inputs
    steps = 10 ** 12
    n = 50
    # solve
    precompute_p2_position(n)
    sol = solve(steps)
    end = time.time()
    print("Solution: %d, %d (time elapsed: %.2f seconds)" %(sol[0], sol[1], end - start))

if __name__ == "__main__":
    main()


