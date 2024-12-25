import time
import math

# found empirically on smallest number of balls that the best arrangement is
# of the form [49, 47, ... 31, 30, 32, 32, ..., 50]
def build_arrangement(shortest_ball, number_of_balls):
    shortest_ball = 30
    number_of_balls = 21
    end = shortest_ball + number_of_balls - 1
    array = [shortest_ball]
    for v in range(shortest_ball, end, 2):
        array.insert(0, v + 1)
        array.append(v + 2)
    return array

def compute_length(arr):
    n = len(arr)
    total_length = arr[0] + arr[-1]
    for i in range(0, n - 1):
        r1 = arr[i]
        r2 = arr[i + 1]
        shared_length = math.sqrt((r1 + r2) ** 2 - (100 - r1 - r2) ** 2)
        total_length += shared_length
    return total_length

def main():
    start = time.time()
    # inputs
    number_of_balls = 21
    shortest_ball = 30
    # solve
    array = build_arrangement(30, 21)
    sol = compute_length(array)
    sol = round(sol * 1e3) # solution in micrometers rounded to the nearest integer
    end = time.time()
    print("Solution: %d (time elapsed: %.2f seconds)" %(sol, end - start))

if __name__ == "__main__":
    main()