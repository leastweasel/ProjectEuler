import math

value = str(math.factorial(100))

total = 0

for c in value:
    total += int(c)
    
print(total)
