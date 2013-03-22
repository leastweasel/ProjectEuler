def isPalindrome(candidate):
    candidateStr = str(candidate)
    stringLen = len(candidateStr)

    midPoint = stringLen // 2
    rangeUp = list(range(0, midPoint+1))

    for x in rangeUp:
        if candidateStr[x] != candidateStr[stringLen-(x+1)]:
            return False
    
    return True

maxPalindrome = 0

for x in range(100,1000):
	for y in range(x,1000):
		candidate = x*y
		
		if isPalindrome(candidate):
			if candidate > maxPalindrome:
				maxPalindrome = candidate

print(maxPalindrome)
