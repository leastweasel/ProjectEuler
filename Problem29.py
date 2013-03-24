from Euler import SieveOfEratosthenes

maxIndex = 100
minIndex = 2

allNumbersToCheck = range(minIndex, maxIndex+1)

s = SieveOfEratosthenes(maxIndex)
primes = []
totalCombinations = (maxIndex-1) ** 2
greaterPowers = []

def getGreaterPowers(ofNumber):
    powers = []
    
    for candidatePower in allNumbersToCheck:
        powerValue = ofNumber ** candidatePower
        
        if powerValue <= maxIndex:
            powers.append((ofNumber, candidatePower, powerValue))
        else:
            break
            
    return powers

def getRoots(candidate):
    roots = []
    
    for greaterPower in greaterPowers:
        if candidate == greaterPower[2]:
            roots.append(greaterPower)
            
    return roots

def isDuplicate(powerToRaiseNumberTo, rootOfNumberBeingRaised):
    totalPowerOfRoot = powerToRaiseNumberTo * rootOfNumberBeingRaised[1]
    
    for i in range(1, rootOfNumberBeingRaised[1]):
        div, mod = divmod(totalPowerOfRoot, i)
        
        if mod == 0:
            if div <= maxIndex:
                return True

    return False

for prime in s:
    primes.append(prime)

for numberToRaise in allNumbersToCheck:
    if numberToRaise not in primes:
        roots = getRoots(numberToRaise)

        if len(roots) > 0:
            for powerToRaiseTo in allNumbersToCheck:
                for root in roots:
                    if isDuplicate(powerToRaiseTo, root):
                        totalCombinations -= 1
                        # print("Ignoring",root[2],"(=",root[0],"**",root[1],") **",powerToRaiseTo,"=",root[2] ** powerToRaiseTo)
                        break

    greaterPowers.extend(getGreaterPowers(numberToRaise))
    
# print("Greater powers are:", greaterPowers)
print("Total combinations =", totalCombinations)