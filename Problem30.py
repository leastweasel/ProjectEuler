#digitPowers = [0 ** 5, 1 ** 5, 2 ** 5, 3 ** 5, 4 ** 5, 5 ** 5, 6 ** 5, 7 ** 5, 8 ** 5, 9 ** 5]

def calculateSumOfDigits(i):
	numberAsStr = str(i)
	sumOfDigits = 0;
	
	for d in numberAsStr:
		sumOfDigits += digitPowers[ord(d) - ord('0')]
		
	return sumOfDigits

digitPowers = []

power = 5

for i in range(0, 10):
	digitPowers.append(i ** power)

sumOfMatchingNumbers = 0
	
for i in range(1, 10 ** 6):
	sumOfDigits = calculateSumOfDigits(i)
	
	if i != 1 and sumOfDigits == i:
		print(i)
		sumOfMatchingNumbers += i
		
print("Sum of matching numbers:", sumOfMatchingNumbers)