from Euler import TriangularNumbers, PrimeFactorisor

def calculateNumberOfDivisors(n):
    pf = PrimeFactorisor(n)
    primeFactors = pf.getPrimeFactors()
    
    factorCounts = {}
    
    for f in primeFactors:
        if f in factorCounts:
            factorCounts[f] = factorCounts[f] + 1
        else:
            factorCounts[f] = 1

    numDivisors = 0

    for f in factorCounts:
        # print "Factor count:", f, " = ", factorCounts[f]

        if numDivisors == 0:
            numDivisors = factorCounts[f] + 1
        else:
            numDivisors *= (factorCounts[f] + 1)
            
    return numDivisors

t = TriangularNumbers(15000)
maxDivisors = 0

for n in t:
    numDivisors = calculateNumberOfDivisors(n)
    #print "Triangular number",n,"has",numDivisors,"divisors" 

    if numDivisors > maxDivisors:
        maxDivisors = numDivisors
        
    if numDivisors > 500:
        print("Triangular number",n,"has",numDivisors,"divisors") 
        
print("Maximum number of divisors = ",maxDivisors)