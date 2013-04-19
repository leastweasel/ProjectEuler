class Reciprocaliser:
    def __init__(self, maxLength):
        self.maxLength = maxLength

    def reciprocalise(self, number):
        self.quotient = ""
        remainder = number
        dividend = 1
        
        for n in range(1, self.maxLength+1):
            dividend *= 10
            quot, rem = divmod(dividend, number)
            
            self.quotient += str(quot)
            dividend = rem
            
            if rem == 0:
                break
                
        return self.quotient

def checkNumberWithCandidate(numberAsStr, candidateStr):
    candidateStrLen = len(candidateStr)
    numberAsStrLen = len(numberAsStr)
    recursCount = 0
    
    for ix in range(0, numberAsStrLen, candidateStrLen):
        if ix + candidateStrLen < numberAsStrLen:
            if numberAsStr[ix:ix+candidateStrLen] != candidateStr:
                return None
            else:
                recursCount += 1

    if recursCount > 1:
        return candidateStr
    else:
        return None

def checkNumber(numberAsStr):
    halfLength = len(numberAsStr) // 2
    
    for l in range(0, halfLength):
        recurringString = checkNumberWithCandidate(numAsStr, numAsStr[0:l+1])
        
        if recurringString is not None:
            return recurringString

    return None
           
r = Reciprocaliser(2000)
maxLength = 0
winningNumber = 0

for n in range(2,1000):
    numAsStr = r.reciprocalise(n)
    #numAsStr = "14285714285714"

    if len(numAsStr) == 2000:
        recurringString = checkNumber(numAsStr)
    
        if recurringString is not None:
            winningStr = recurringString
            candidateLength = len(winningStr)
            #print ("Recurs:", n, numAsStr, winningStr, candidateLength)
            print ("Recurs:", n, winningStr, candidateLength)
        
            if candidateLength > maxLength:
                maxLength = candidateLength
                winningNumber = n

print("Winning number is", winningNumber)
print("Recurrence length is", maxLength)
print("Original number is", r.reciprocalise(winningNumber))
