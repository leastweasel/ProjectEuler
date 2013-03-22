from Euler import SieveOfEratosthenes, PrimeFactorisor

# Set up the value whose highest prime factor we're after, and the highest possible prime we'll look for on the first
# attempt, that being the sqaure root of the number we're trying to factorise. If we fail to find to find all of them
# then have another go with what's left.
pf = PrimeFactorisor(600851475143)
print(pf.getPrimeFactors())
