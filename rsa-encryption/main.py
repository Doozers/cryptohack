# N = p * q -> product of 2 primes
# RSA pubkey == (N, e)

# to_encrypt^ex % modulus

e = 0x10001
N = 17 * 23

res = pow(12, e, N)

print(res)

