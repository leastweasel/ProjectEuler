fibA = 1
fibB = 1
term = 3

while True:
    fibC = fibA + fibB
    
    if len(str(fibC)) >= 1000:
        print(fibC)
        print("Term:", term)
        break
    else:
        fibA = fibB
        fibB = fibC
        term += 1