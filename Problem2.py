previousTerm = nextTerm = 1
evensSum = 0

while nextTerm < 4000000:
    evensSum = evensSum + previousTerm + nextTerm
    previousTerm, nextTerm = (2 * nextTerm) + previousTerm, (3 * nextTerm) + (2 * previousTerm)
    
print(evensSum)