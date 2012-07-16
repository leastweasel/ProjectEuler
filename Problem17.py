WordLengthMap = {}
WordLengthMap[0] = ""
WordLengthMap[1] = "one"
WordLengthMap[2] = "two"
WordLengthMap[3] = "three"
WordLengthMap[4] = "four"
WordLengthMap[5] = "five"
WordLengthMap[6] = "six"
WordLengthMap[7] = "seven"
WordLengthMap[8] = "eight"
WordLengthMap[9] = "nine"
WordLengthMap[10] = "ten"
WordLengthMap[11] = "eleven"
WordLengthMap[12] = "twelve"
WordLengthMap[13] = "thirteen"
WordLengthMap[14] = "fourteen"
WordLengthMap[15] = "fifteen"
WordLengthMap[16] = "sixteen"
WordLengthMap[17] = "seventeen"
WordLengthMap[18] = "eighteen"
WordLengthMap[19] = "nineteen"
WordLengthMap[20] = "twenty"
WordLengthMap[30] = "thirty"
WordLengthMap[40] = "forty"
WordLengthMap[50] = "fifty"
WordLengthMap[60] = "sixty"
WordLengthMap[70] = "seventy"
WordLengthMap[80] = "eighty"
WordLengthMap[90] = "ninety"

def hundredLengthFor(number):
    contribution = 0
    hundredNumber, hundredRemainder = divmod(number, 100)

    if hundredNumber == 10:
        contribution = 11 # len("onethousand")
    elif hundredNumber > 0:
        contribution = len(WordLengthMap[hundredNumber]) + 7 # len("hundred")
        
        if hundredRemainder > 0:
            contribution += 3   # len("and")
            
    return contribution

def tenLengthFor(number):
    contribution = 0
    hundredRemainder = number % 100
    tenNumber, tenRemainder = divmod(hundredRemainder, 10)

    if hundredRemainder < 21:
        contribution = len(WordLengthMap[hundredRemainder])
    else:
        contribution = len(WordLengthMap[(tenNumber * 10)])
        contribution += len(WordLengthMap[tenRemainder])
            
    return contribution
        
total = 0

for i in range(1000):
    total += hundredLengthFor(i+1) + tenLengthFor(i+1)

print total
        
print (hundredLengthFor(1000) + tenLengthFor(1000))