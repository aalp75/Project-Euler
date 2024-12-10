# Project Euler 217

MOD = 3 ** 15

N = 47
max_sum_digit = (9 * N) // 2

count = [[0 for i in range(max_sum_digit + 1)] for j in range(N + 1)]
# count[i][j] = numbers of number with length less than i where the digits are summing to j

count[0][0] = 1
count[1][:10] = [1 for k in range(10)]

for i in range(2, N + 1): # Loop on the length of numbers
    for j in range(max_sum_digit + 1): # Loop on the value of the sum
        for d in range(0, 10): # Loop on the 1st digit: 1 to 9
            if j - d < 0:
                break
            # first digit is d then the last i - 1 numbers should sum to j - d
            count[i][j] = (count[i][j] + count[i - 1][j - d]) % MOD

dp_sum = [[0 for i in range(max_sum_digit + 1)] for j in range(N + 1)]
# dp_sum[i][j] = sum of all numbers of size less than i with all digits summing to j

dp_sum[1][:10] = [k for k in range(10)]

for i in range(2, N + 1): # Loop on the length of numbers
    p10 = 10 ** (i - 1) % MOD
    for j in range(max_sum_digit + 1): # Loop on the value of the sum
        dp_sum[i][j] = dp_sum[i - 1][j]
        for d in range(1, 10): # Loop on the 1st digit: 1 to 9
            if j - d < 0:
                break
            dp_sum[i][j] = (dp_sum[i][j] + d * p10 * count[i - 1][j - d] + dp_sum[i - 1][j - d]) % MOD
    
sol = 45 # for the 1 digits

for i in range(2, N + 1): # Loop on the length of numbers
    half = i // 2
    p10 = 10 ** (i - 1) % MOD
    p10_half = 10 ** half % MOD
    for j in range(max_sum_digit + 1): # Loop on the value of the sum
        for d in range(1, 10): # Loop on the 1st digit
            if j - d < 0:
                break
            if count[half - 1][j - d] == 0 or count[half][j] == 0:
                continue
            if i % 2 == 0: # if i is even
                    sol = (sol + d * p10 * count[half - 1][j - d] * count[half][j]) % MOD
                    sol = (sol + dp_sum[half - 1][j - d] * p10_half * count[half][j]) % MOD
                    sol = (sol + dp_sum[half][j] * count[half - 1][j - d]) % MOD
            else: # if i is odd
                for d2 in range(0, 10): # Loop on the digit of the midle: 0 to 9
                        sol = (sol + d * p10 * count[half - 1][j - d] * count[half][j]) % MOD
                        sol = (sol + dp_sum[half - 1][j - d] * 10 * p10_half * count[half][j]) % MOD
                        sol = (sol + d2 * p10_half * count[half - 1][j - d] * count[half][j]) % MOD
                        sol = (sol + dp_sum[half][j] * count[half - 1][j - d]) % MOD

print("Solution: %d" %(sol))