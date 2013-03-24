from Euler import SieveOfEratosthenes

maxB = 1000
minB = -999
primes = SieveOfEratosthenes(3000).asList()

def getNumberOfConsecutivePrimes(a, b):
    n = 0
    
    while True:
        value = (n * n) + (a * n) + b
        
        if value not in primes:
            break

        n += 1

    return n
    
maxNumberOfPrimes = 0
bestPair = 0,0

for a in range(minB, maxB):
    for b in range(minB, maxB):
        if b in primes:
            numberOfPrimes = getNumberOfConsecutivePrimes(a,b)

            if numberOfPrimes > maxNumberOfPrimes:
                maxNumberOfPrimes = numberOfPrimes
                bestPair = a,b
            
print("Maximum number of consecutive primes is: ", maxNumberOfPrimes)
print("Best pair is: ",bestPair,"=",(bestPair[0]*bestPair[1]))