from Euler import TriangularNumbers, PrimeFactorisor, CombinationsGenerator

def calculateNumberOfDivisors(n):
    pf = PrimeFactorisor(n)
    primeFactors = pf.getPrimeFactors()
    
    cg = CombinationsGenerator(primeFactors)
    
    divisors = [1]
    divisors.extend(cg.getUniqueCombinations())
    
    return divisors

t = TriangularNumbers(10)

for n in t:
    print calculateNumberOfDivisors(n)
