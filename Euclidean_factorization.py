from decimal import Decimal, getcontext
import math
import sympy

n = int(input("enter N: "))

getcontext().prec = 2048
decimal_number = Decimal(n)
sqrt_result = decimal_number.sqrt()
sqrt_n = int(sqrt_result)

s2 = sqrt_n * sqrt_n

while s2 < n:
    sqrt_n+=1
    s2 = sqrt_n * sqrt_n

s = sqrt_n
t = math.isqrt(s2 - n)
while t*t != (s2 - n):
    s += 1
    s2 = s * s
    t = math.isqrt(s2-n)

p = s + t
q = s - t
if sympy.isprime(p) and sympy.isprime(q) and p*q==n:
    print("waalllaaa !! found it")
print("p = ",p)
print("q = ",q)
print(f"p is prime {sympy.isprime(p)}, q is prime {sympy.isprime(q)}")
print(f"p*q=n : {p*q==n}")