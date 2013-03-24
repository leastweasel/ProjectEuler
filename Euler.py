from bitarray import bitarray
from math import sqrt

class SieveOfEratosthenes:
    """A class for generating prime numbers.
    
    An iterator that returns all prime numbers up to, and including, a given number.
    Uses a Sieve of Eratosthenes algorithm to calculate the primes, with an initial
    bit of wheel factorisation to discard two thirds of the candidates.
    """
    def __init__(self, maxCandidate):
        """Set up the maximum prime that will be returned."""
        self.maxCandidate = maxCandidate
        self.primeCandidates = maxCandidate * bitarray('0')
        self.currentIndex = 1;
        self.setupCandidatePrimes()

    def __iter__(self):
        return self
        
    def setupCandidatePrimes(self):
        """Set up the bit array of possible primes.
        
        Use wheel factorisation to throw away two thirds of the possible candidates (using n = 2 * 3).
        """
        if self.maxCandidate > 1:
            self.primeCandidates[1] = True
        
            if self.maxCandidate > 2:
                self.primeCandidates[2] = True
            
                if self.maxCandidate > 4:
                    self.primeCandidates[4] = True
                    self.primeCandidates[6::6] = True
                    self.primeCandidates[10::6] = True

    def __next__(self):
        """Get the next prime, raising a StopIteration exception if there are no more."""
        if self.currentIndex >= self.maxCandidate:
            raise StopIteration
            
        nextPrimeToReturn = self.currentIndex + 1
        self.crossOffPrimeMultiples(nextPrimeToReturn)
        
        while self.currentIndex < self.maxCandidate:
            if self.primeCandidates[self.currentIndex]:
                break
                
            self.currentIndex += 1
        
        return nextPrimeToReturn
            
    def crossOffPrimeMultiples(self, prime):
        """Discard all multiples of the given prime from the list of candidates."""
        index = self.currentIndex
    
        while index < self.maxCandidate:
            self.primeCandidates[index] = False
            index += prime

class PrimeFactorisor:
    """A class that can factorise a given number into its constituent primes."""
    def __init__(self, numberToFactorise):
        self.numberToFactorise = numberToFactorise
        self.factorisationRemainder = numberToFactorise
        self.primeFactors = []

    def getPrimeFactors(self):
        """Get all of the prime factors of the number, including duplicates."""
        ok = False
        maxCandidate = int(sqrt(self.numberToFactorise))

        while not ok:
            s = SieveOfEratosthenes(maxCandidate)
            
            # print "Max candidate is ", maxCandidate
            self.addPrimeFactors(s)
            ok = self.checkResult()
            maxCandidate = self.factorisationRemainder
            
        return self.primeFactors
            
    def addPrimeFactors(self, sieve):
        """Add all the prime factors of the current remainder from the given sieve."""
        for prime in sieve:
            while self.factorisationRemainder % prime == 0:
                self.primeFactors.append(prime)
                self.factorisationRemainder = int(self.factorisationRemainder / prime)

    def checkResult(self):
        """Check that we've found all the factors and, if so, display the highest."""
        productOfFoundFactors = 1;
        ok = False

        # print "Remainder is ", self.factorisationRemainder
    
        for factor in self.primeFactors:
            productOfFoundFactors *= factor
        
        if productOfFoundFactors == self.numberToFactorise:
            # print "Found factors:", self.primeFactors
            ok = True
        # else:
            # print "Not all factors found - keep going..."
    
        return ok

class TriangularNumbers:
    """A class for generating triangular numbers.
    
    An iterator that returns triangular numbers. It can be configured to return
    numbers up to, and including, a given number, or to iterate indefinitely.
    """
    def __init__(self, maxCandidate):
        """Set up the maximum prime that will be returned."""
        print("Max Candidate:", maxCandidate)
        self.maxCandidate = maxCandidate
        self.currentIndex = 0;
        self.currentNumber = 0;

    def __iter__(self):
        return self
        
    def __next__(self):
        """Get the next number, raising a StopIteration exception if there are no more."""
        if self.maxCandidate != None and self.currentIndex >= self.maxCandidate:
            raise StopIteration
            
        self.currentIndex += 1
        self.currentNumber += self.currentIndex
        
        return self.currentNumber

class CombinationsGenerator:
    """docstring for CombinationsGenerator"""
    def __init__(self, source):
        self.source = source

    def getAllCombinations(self):
        return []
        
    def getUniqueCombinations(self):
        return set(self.getAllCombinations())
        
    def getSomething(lenth):
        if length <= 1:
            return "Hello"
        else:
            getSomething(length -1)