import time
import numpy as np

# The game can be represented as a Markov chain where state i represents the distance between player 1 
# and player 2. That gives a Markov chain with 51 states (0 to 50 - the maximum distance) with a transition
# matrix P clearly defined that we can simulate

def solve():
    start = time.time()
    P = np.zeros((51, 51))
    P[50][50] = 1 / 2
    P[50][49] = 4 / 9
    P[50][48] = 2/ 36
    P[49][50] = 2 / 9
    P[49][49] = 1 / 2 + 1 / 36
    P[49][48] = 2 / 9
    P[49][47] = 1 / 36
    P[1][3] = 1 / 36
    P[1][2] = 2 / 9
    P[1][1] = 1 / 2 + 1 / 36
    P[1][0] = 2 / 9
    P[0][0] = 1
    for i in range(2, 49):
        P[i][i - 2] = 1 / 36
        P[i][i - 1] = 2 / 9
        P[i][i] = 1 / 2
        P[i][i + 1] = 2 / 9
        P[i][i + 2] = 1 / 36

    position = np.zeros((1, 51))
    position[0][50] = 1

    curr = position
    cum_prob = 0
    sol = 0.0
    for i in range(1, 100000):
        curr = curr @ P
        prob = curr[0][0] - cum_prob
        sol += i * prob
        cum_prob = curr[0][0]
    sol = round(sol, 6)
    end = time.time()
    print("Solution: %f (time elapsed: %.2f seconds)" %(sol, end - start))

if __name__ == "__main__":
    solve()
