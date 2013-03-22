from collections import deque

class Answer:
    def __init__(self, maxLength):
        """Set up the maximum length of the queue."""
        self.maxLength = maxLength
        self.answer = deque()
        self.carry = 0

    def append(self, sum):
        tens, remainder = divmod(sum + self.carry, 10)
        
        if len(self.answer) >= self.maxLength:
            self.answer.popleft()
        
        self.answer.append(str(remainder))
        self.carry = tens
        
        # print "Append digit:", str(remainder), " and carry:", str(tens)

    def firstDigits(self):
        while self.carry > 0:
            self.append(0)
        
        return reverseAndPadNumber(self.answer, self.maxLength), self.carry
        
def readNumbersToSum(filename):
    numbersToSum = []
    maxLength = 0
    
    with open(filename, 'r') as f:
        for longNumber in f:
            longNumber = longNumber.strip()
            
            if len(longNumber) > maxLength:
                maxLength = len(longNumber)

            numbersToSum.append(longNumber)

    print("Longest number is",maxLength,"digits long")
    
    return reverseAndPadNumbers(numbersToSum, maxLength)

def reverseAndPadNumbers(numbersToSum, maxLength):
    reversedNumbers = []
    
    for longNumber in numbersToSum:
        reversedNumbers.append(reverseAndPadNumber(longNumber, maxLength))
    
    return reversedNumbers

def reverseAndPadNumber(numberToReverse, length):
    reversedNumber = ""

    for i in range(len(numberToReverse), 0, -1):
        reversedNumber += numberToReverse[i-1]

    for i in range(length, len(numberToReverse), -1):
        reversedNumber += "0"

    return reversedNumber
    
def sumNumbers(numbersToSum, lengthOfInterest):
    numberLength = len(numbersToSum[0])
    ans = Answer(lengthOfInterest)

    for position in range(numberLength):
        sumAtPosition = sumDigitsAtPosition(numbersToSum, position)
        # print "Total at position",str(position),"is",str(sumAtPosition)
        
        ans.append(sumAtPosition)
    
    return ans.firstDigits()

def sumDigitsAtPosition(numbersToSum, position):
    total = 0
    
    for number in numbersToSum:
        total += int(number[position])

    return total
    
numbersToSum = readNumbersToSum('Problem13.txt')

print("Read",len(numbersToSum),"numbers from file")

if len(numbersToSum) > 0:
    print("First number is:", numbersToSum[0])
    
    firstDigits, carry = sumNumbers(numbersToSum, 10)
    print("First digits of sum:", firstDigits)
    print("Carry:", carry)