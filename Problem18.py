class TreeNode:
    def __init__(self, value):
        self.leftNode = None
        self.rightNode = None
        self.value = value
        self.valueAsParent = 0
    
def readNumberTree(filename):
    rows = []
    
    with open(filename, 'r') as f:
        for line in f:
            rowOfNodes = []
            rowOfStrings = line.strip().split()
            nodeIndex = 0
            parentRowIndex = len(rows) - 1
            
            for numStr in rowOfStrings:
                thisNode = TreeNode(int(numStr))
                rowOfNodes.append(thisNode)
                
                if parentRowIndex >= 0:
                    if nodeIndex < len(rowOfStrings) - 1:
                        parentNode = rows[parentRowIndex][nodeIndex]
                        parentNode.leftNode = thisNode
                        
                    if nodeIndex > 0:
                        parentNode = rows[parentRowIndex][nodeIndex-1]
                        parentNode.rightNode = thisNode
                    
                nodeIndex += 1

            rows.append(rowOfNodes)

    return rows

def processRows(rows):
    maxPath = 0
    
    for rowNumber in range(len(rows), 0, -1):
        rowOfNodes = rows[rowNumber-1]
        
        for node in rowOfNodes:
            maxValue = node.value
            
            if node.leftNode != None:
                maxValue = node.value + node.leftNode.valueAsParent
                
            if node.rightNode != None:
                maxValue = max(maxValue, node.rightNode.valueAsParent + node.value)

            node.valueAsParent = maxValue
            
    return rows[0][0].valueAsParent
    
print("Problem 18:", processRows(readNumberTree("Problem18.txt")))
print("Problem 67:", processRows(readNumberTree("Problem67.txt")))
