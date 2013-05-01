def numberOfCombinations(target, coins):
    if len(coins) == 0:
        return 0

    if target == 0:
        return 0

    combinations = 0
    instances = target // coins[0]

    if target % coins[0] == 0:
        #print("Made", target, "from", coins, "with", instances, "instances remaining")
        combinations += 1

    for i in range(instances, 0, -1):
        combinations += numberOfCombinations(target - (i * coins[0]), coins[1:])

    return combinations + numberOfCombinations(target, coins[1:])
 
target = 200
coins = [200, 100, 50, 20, 10, 5, 2, 1]
 
num = numberOfCombinations(target, coins)
print("Number of combinations", num)