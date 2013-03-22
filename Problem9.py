for c in range(499, 334, -1):
	for b in range(c-1, (1000 - c) / 2, -1):
		a = 1000 - c - b
		
		if a ** 2 + b ** 2 == c ** 2:
			print(a * b * c)