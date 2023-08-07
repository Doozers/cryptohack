## it exist a quadratic redisue for a number "X" only if there is an "A" such that a^2 = x mod p

p = 29

def find_quadratic_residue(x):
    i = 2
    while i < p-1:
        if (i**2) % p == (x % p):
            return i
        i += 1
    return -1

res = find_quadratic_residue(6)

if res == -1:
    print("No solution")
else:
    print("result is ", res)
