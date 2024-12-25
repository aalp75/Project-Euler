import time

# using the fact the number of possible value is finite and pigeon hole principle
# all Tribonacci sequences modulo mod are periodic (same argument as Pisano period)
# with a period less than mod ^ 3, in fact is way less
def check_divisibility(mod):
    T1 = 1
    T2 = 1
    T3 = 1
    seq = [T1, T2, T3]
    mem = set((T1, T2, T3))
    is_div = False
    while True:
        TN = (T1 + T2 + T3) % mod
        seq.append(TN)
        T1 = T2
        T2 = T3
        T3 = TN
        if TN == 0:
            is_div = True
        if (T1, T2, T3) in mem:
            return is_div
        mem.add((T1, T2, T3))
    return is_div

def main():
    start = time.time()
    # inputs
    n = 124
    # solve
    count = 0
    N = n * 100 # upper bound
    for i in range(3, N, 2): # loop on odd numbers
        is_divisible = check_divisibility(i)
        if not is_divisible:
            count += 1
        if count == n:
            sol = i
            break       
    end = time.time()
    print("Solution: %d (time elapsed: %.2f seconds)" %(sol, end - start))

if __name__ == "__main__":
    main()