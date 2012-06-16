n = 100
nTimesNPlus1 = n * (n + 1)
difference = 0

for x in range (1,n + 1):
	difference += x * (nTimesNPlus1 - (x * (x + 1)))
	
print difference