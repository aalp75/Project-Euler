import time

def solve(N):
    cost = [0] * 100 # enough space
    cost[1] = 1
    cost[4] = 1
    score = 5
    count = 2
    for i in range(1, N):
        needed = N - count
        available = min(cost[i], needed)
        score -= available * i
        cost[i + 1] += available
        cost[i + 4] += available
        score += available * (i + 1) + available * (i + 4)
        count += available
        if count == N:
            break
    return score

def main():
    start = time.time()
    N = 10 ** 9
    sol = solve(N)
    end = time.time()
    print("Solution: %d (time elapsed: %.2f seconds)" %(sol, end - start))

if __name__ == "__main__":
    main()

