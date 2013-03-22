from Euler import SieveOfEratosthenes

s = SieveOfEratosthenes(1999999)
sumOfPrimes = 0

for prime in s:
    sumOfPrimes += prime

print("Sum =", sumOfPrimes)
