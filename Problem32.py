def isPandigital(multiplicand, multiplier, product):
    multiplicandStr = str(multiplicand)
    multiplierStr = str(multiplier)
    productStr = str(product)
    
    if len(multiplicandStr) + len(multiplierStr) + len(productStr) == 9:
        digits = set()
        
        addDigitsToSet(digits, multiplicandStr)
        addDigitsToSet(digits, multiplierStr)
        addDigitsToSet(digits, productStr)
        
        if len(digits) == 9:
            return True
            
    return False

def addDigitsToSet(digitSet, numberStr):
    for c in numberStr:
        if c != '0':
            digitSet.add(c)

pandigitals = set()

for a in range(1, 5000):
    for b in range(1, 5000):
        product = a*b
        
        if isPandigital(a, b, product):
            print(a, "*", b, "=", product)
            pandigitals.add(product)

print("Got", len(pandigitals), "pandigitals")

totalProducts = 0

for i in pandigitals:
    totalProducts += i
    
print("Total: ", totalProducts)