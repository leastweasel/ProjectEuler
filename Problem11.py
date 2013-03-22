class SequenceGenerator:
    def __init__(self, xDisplacement, yDisplacement):
        self.xDisplacement = xDisplacement
        self.yDisplacement = yDisplacement
    
    def createSequence(self, x, y, size):
        sequence = []
        currentPoint = ()
        
        for i in range(size):
            currentPoint = (x + ((i + 1) * self.xDisplacement), y + ((i + 1) * self.yDisplacement))
            sequence.append(currentPoint)
        
        return sequence

class MaximumCounter:
    def __init__(self, grid):
        self.grid = grid
        self.maximumValue = 0
        self.maximumSequence = None
        
    def evaluateSequence(self, sequence):
        value = 1
            
        for x, y in sequence:
            value *= self.grid.gridCells[y][x]
                
        if value > self.maximumValue:
            self.maximumValue = value
            self.maximumSequence = sequence
            print(self.maximumValue, self.maximumSequence)

class Grid(object):
    def __init__(self, gridCells):
        self.gridCells = gridCells

    def isValidSequence(self, seq):
        for x, y in seq:
            if x < 0 or y < 0 or x >= len(self.gridCells[1]) or y >= len(self.gridCells):
                return False
    
        return True
        
gridCells = []

gridCells.append([8, 0o2, 22, 97, 38, 15, 00, 40, 00, 75, 0o4, 0o5, 0o7, 78, 52, 12, 50, 77, 91, 8])
gridCells.append([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 0o4, 56, 62, 00])
gridCells.append([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 0o3, 49, 13, 36, 65])
gridCells.append([52, 70, 95, 23, 0o4, 60, 11, 42, 69, 24, 68, 56, 0o1, 32, 56, 71, 37, 0o2, 36, 91])
gridCells.append([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
gridCells.append([24, 47, 32, 60, 99, 0o3, 45, 0o2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
gridCells.append([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
gridCells.append([67, 26, 20, 68, 0o2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
gridCells.append([24, 55, 58, 0o5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
gridCells.append([21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95])
gridCells.append([78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 0o3, 80, 0o4, 62, 16, 14, 9, 53, 56, 92])
gridCells.append([16, 39, 0o5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57])
gridCells.append([86, 56, 00, 48, 35, 71, 89, 0o7, 0o5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
gridCells.append([19, 80, 81, 68, 0o5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 0o4, 89, 55, 40])
gridCells.append([0o4, 52, 8, 83, 97, 35, 99, 16, 0o7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
gridCells.append([88, 36, 68, 87, 57, 62, 20, 72, 0o3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
gridCells.append([0o4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
gridCells.append([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 0o4, 36, 16])
gridCells.append([20, 73, 35, 29, 78, 31, 90, 0o1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 0o5, 54])
gridCells.append([0o1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 0o1, 89, 19, 67, 48])

grid = Grid(gridCells)

generators = []
generators.append(SequenceGenerator(-1, 0))
generators.append(SequenceGenerator(0, -1))
generators.append(SequenceGenerator(-1, -1))
generators.append(SequenceGenerator(1, -1))

maxCounter = MaximumCounter(grid)

for y in range(20):
    for x in range(20):
        for g in generators:
            seq = g.createSequence(x, y, 4)
            
            if grid.isValidSequence(seq):
                maxCounter.evaluateSequence(seq)

print(maxCounter.maximumValue)
print(maxCounter.maximumSequence)