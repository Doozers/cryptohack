# modular multiplicative inverse => X == ax / m == 1
# can be found with euclidean algorythm

e = 65537
N = (857504083339712752489993810777-1)*(1029224947942998075080348647219-1) # euler totien

res = pow(e, -1, N)

print(res)

