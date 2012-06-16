def findNumberOfFactorInstances(factor, maximumNumber):
    (numberOfInstances, remainder) = divmod(maximumNumber, factor)

    if remainder == 0:
        numberOfInstances = numberOfInstances - 1
        
    return numberOfInstances
    
def findSumOfFactors(factor, numberOfInstances):
    return factor * numberOfInstances * (numberOfInstances + 1) / 2

def getCommonProducts(factors, maximumNumber):
    products = []
    
    product = factors[0] * factors[1]
    
    if product < maximumNumber:
        products.append(product)
    
    return products
    
factors = [3,5]
maximumNumber = 1000
total = 0

for factor in factors:
    numberOfInstances = findNumberOfFactorInstances(factor, maximumNumber)
    total = total + findSumOfFactors(factor, numberOfInstances)

commonProducts = getCommonProducts(factors, maximumNumber)
    
for product in commonProducts:
    numberOfInstances = findNumberOfFactorInstances(product, maximumNumber)
    total = total - findSumOfFactors(product, numberOfInstances)
        
print total