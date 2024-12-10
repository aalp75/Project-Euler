from math import gcd

# using the Euclid's formula to generate Pythagorean triples we get a=2mn, b=m*m-n*n, c=m*m-n*n
# repplaying this logic on the fact that c is a perfect square so c^2=m^2-n^2 we get a close form for a*b with respect to
# x and y that we can use the check the area condition of the triangle

sol = 0
for x in range(42):
    for y in range(42):
        rel = (x * x - y * y) * x * y * ((2 * x * y) ** 2 - (x * x - y * y) ** 2)
        if rel % 42 != 0:
            sol += 1
            
print("Solution:", sol)

# generate all primtive Pythagorean triples up to k

k = 100

count = 1
for m in range(k):
    for n in range(1, m):
        c = m * m + n * n
        if c > k:
            break
        if gcd(n, m) != 1:
            continue
        a = 2 * m * n
        b = m * m - n * n
        
        count += 1
        print("(%d, %d, %d)" %(a, b, c))