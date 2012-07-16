def initialiseRoutingTable(gridSize):
    # Set up the routing table to be a square of the appropriate size.
    routingTable = [[0 for x in range(gridSize+1)] for x in range(gridSize+1)]

    # Row 1 and Column 1 are full of ones.
    for i in range(0, gridSize+1):
        routingTable[0][i] = 1
        routingTable[i][0] = 1

    # The remaining cells have a value equal to the sum of the cell above and to the left of the current one.
    for x in range(1, gridSize+1):
        for y in range(1, gridSize+1):
            routingTable[x][y] = routingTable[x][y-1] + routingTable[x-1][y]

    return routingTable

def setUpCoordinates(gridSize):
    coords = []
    
    for i in range(0, gridSize+1):
        coord = (i, gridSize-i)
        coords.append(coord)
        
    return coords
      
gridSize = 20

routingTable = initialiseRoutingTable(gridSize)
coords = setUpCoordinates(gridSize)

total = 0

for coord in coords:
    cellValue = routingTable[coord[0]][coord[1]]
    total += (cellValue ** 2)
    
print total