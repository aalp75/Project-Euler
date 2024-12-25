import math
import numpy as np
import time
from scipy import integrate

# compute the area as the difference between the area under the blancmange curve 
# from 0 to 0.5 (0.25) and the area under the zone delimited by the minimum between
# the blancmange curve and the cercle of center (1 / 4, 1 / 2) and radius 1 /4

# different method are available to compute numerically the integral
# 1 - scipy integrate quad, which gives enough accuracy with the correct parameters
# 2 - Riemann sum using mid point, it provides enough accuracy with the correct dx (1e-5)
# 3 - Monte carlo, it doesn't give enough accuracy, enough with a large number of simulations

def s(x):
    return min(abs(math.floor(x) - x), abs(math.ceil(x) - x))

def blancmange_curve(x, N=60): # double precision: 2 ^ 60
    val = 0
    p2 = 1.0
    for n in range(N + 1):
        val += s(p2 * x) / p2
        p2 *= 2
    return val

# cercle of centre (a, b) and radius r
def cercle_curve(x, a, b, r):
    return -math.sqrt(r * r - (x - a) ** 2) + b

def lower_part(x):
    return min(blancmange_curve(x), cercle_curve(x, 1 / 4, 1 / 2, 1 / 4))

# Riemann sum
def riemann_sum(a, b, dx=1e-5):
    x_start = a
    x_end = b
    rs = 0
    while x_start < b:
        x_next = min(x_start + dx, x_end)
        x_mid = (x_start + x_next) / 2
        rs += (x_next - x_start) * lower_part(x_mid)
        x_start = x_next 
    return rs

# Monte Carlo
def MC(N=10_000):
    x = np.random.uniform(0, 0.5, N)
    y = np.random.uniform(0, 1, N)
    E = 0
    for i in range(N):
        if y[i] < lower_part(x[i]):
            E += 1
    return E / N / 2

def solve():

    start = time.time()
    low_area = integrate.quad(lower_part, 0, 0.5, limit=1000)
    sol = round(0.25 - low_area[0], 8)
    end = time.time()
    print("Solution scipy: %.8f (time elapsed: %.2f seconds)" %(sol, end - start))

    start = time.time()
    low_area = riemann_sum(0, 0.5, 1e-5)
    sol = round(0.25 - low_area, 8)
    end = time.time()
    print("Solution Riemann sum: %.8f (time elapsed: %.2f seconds)" %(sol, end - start))

    start = time.time()
    low_area = MC(100000)
    sol = round(0.25 - low_area, 8)
    end = time.time()
    print("Solution Monte Carlo: %.8f (time elapsed: %.2f seconds)" %(sol, end - start))

if __name__ == "__main__":
    solve()
        

