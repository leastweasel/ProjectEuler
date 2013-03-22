mostSteps = 0
forStartNumber = 0
        
for startNumber in range(2, 1000000):
    currentNumber = startNumber
    steps = 0

    while currentNumber != 1:
        if currentNumber & 1 == 1:
            currentNumber = currentNumber + currentNumber + currentNumber + 1
        else:
            currentNumber = currentNumber >> 1
            
        steps += 1
        
    if steps > mostSteps:
        mostSteps = steps
        forStartNumber = startNumber
        
print("Longest sequence is",mostSteps,"for starting number",forStartNumber)