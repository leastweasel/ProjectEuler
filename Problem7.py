from Euler import SieveOfEratosthenes

s = SieveOfEratosthenes(200000)
foundNumberOfPrimes = 0

for prime in s:
    foundNumberOfPrimes += 1

    if foundNumberOfPrimes == 10001:
        break;

print "Found", foundNumberOfPrimes, "primes. Maximum is:", prime
