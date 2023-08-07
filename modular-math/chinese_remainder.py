## for a congruence (a1, n1),(a2, n2)...(an, nn) if {n1..nn} are coprimes then it exist a unique solution "x" such that:
## 
## x = a1 mod n1
## 
## x = a2 mod n2
##
## . . .
##
## x = an mod nn

from functools import reduce
import operator

congruences = [(2,5), (3,11), (5,17)]

def chinese_remainder():
    max = reduce(operator.mul, (moduli for _, moduli in congruences))
    for i in range(max):
        if all(i % moduli == remainder for remainder, moduli in congruences):
            return i

print("chinese remainder is", chinese_remainder())
