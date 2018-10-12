import sys
import os
import math

minSize = 0
dimensionType = 0
leaves = {}
module_path = os.path.dirname(__file__)


def getInputs():
    global minSize, dimensionType
    sys.argv.append("2d_small.txt")  # necessary command for debug
    sys.argv.append("1")
    arguments = sys.argv
    if len(arguments) != 3:
        print("Please Enter Correct Inputs !")
        return
    fileName = sys.argv[1]
    minSize = int(sys.argv[2])
    # print(os.path.exists(module_path+"2d_large.txt"))
    # print(module_path+"/"+fileName)
    dataFile = module_path + "/" + fileName  # pycharm can ignore this / , but in terminal cannot
    if not os.path.exists(dataFile):
        print("Please Enter Correct File name !")
        return
    inputData = []
    with open(dataFile, "r") as f:
        for line in f.readlines():
            line = line.strip()
            inputData.append(list(map(float, line.split(" "))))
    dimensionType = int(inputData[0][0])
    dataSet = inputData[1:]
    root = BuildTree(dataSet, 0)
    traversalTreeInPreOrder(root, "")
    printTreeLeavesIO(root)


def printTreeLeavesIO(root):
    choose = str(input("Print tree leaves? (Enter Y for yes, anything else for no): "))
    if choose == "Y" or choose == "y":
        count = 0
        for key, value in leaves.items():
            print(str(count) + ".", key, ":", "Bounding Box: ", getBoundingValue(value))
            # print(str(count) + ".", key, ":", "Bounding Box: ")
            print("Data in Leaf: ", value)
            count += 1
    temp = str(input("Test data? (Enter Y for yes, anything else to quit): "))
    if temp == "Y" or temp == "y":
        Flag = True
        while Flag:
            inputTestFileName = str(input("Name of data-file: "))
            testFileName = module_path + "/" + inputTestFileName
            if not os.path.exists(testFileName):
                print("Please Enter Correct File name !")
                continue
            else:
                print("Correct File")
                testData = []
                with open(testFileName, "r") as f:
                    for line in f.readlines():
                        line = line.strip()
                        testData.append(list(map(float, line.split(" "))))
                testDataDimentionType = testData[0][0]
                if testDataDimentionType != dimensionType:
                    print("Dismatch the Dimentions. ")
                    continue
                testDataSet = testData[1:]
                findNeighbors(root, testDataSet, 0)
            Flag = False
    else:
        print("________________________________")
        print("Goodbye.")
        return


def findNearest(target, nodeSet):
    distances = []
    for node in nodeSet:
        addTemp = 0
        for d in range(dimensionType):
            addTemp += math.pow((node[d] - target[d]), 2)
        distances.append(math.sqrt(addTemp))
    minVal = min(distances)
    minIndex = distances.index(minVal)
    return nodeSet[minIndex]


def calculateL2(node1, node2):
    addTemp = 0
    for d in range(dimensionType):
        addTemp += math.pow((node1[d] - node2[d]), 2)
    return math.sqrt(addTemp)


def findNeighbors(root, testSet, depth):
    for item in testSet:
        print(item, "is in the set:", findNeighborsHelper(root, item, depth))
        nearnest = findNearest(item, findNeighborsHelper(root, item, depth))
        print("Nearest neighbor:", nearnest, "(distance=", calculateL2(nearnest, item), ")")
        print()


def findNeighborsHelper(root, node, depth):
    if root is None:
        return
    nodes = root.nodes
    split = depth % dimensionType
    if len(nodes) == 1 and (root.left is not None and root.right is not None):
        if nodes[0][split] <= node[split]:
            return findNeighborsHelper(root.right, node, depth + 1)

        else:
            return findNeighborsHelper(root.left, node, depth + 1)
    else:
        return nodes


def BuildTree(dataSet, depth):
    if len(dataSet) <= minSize:
        # print("___", dataSet)
        return TreeNode(dataSet)
    else:
        split = depth % dimensionType  # +1 and -1 so I simply ignored it
        dataSet.sort(key=lambda x: x[split])
        left = 0
        right = len(dataSet) - 1
        median = left + int((right - left) / 2)
        parent = TreeNode([dataSet[median]])
        parent.left = BuildTree(dataSet[0:median + 1], depth + 1)  # 0 to (median)
        # if parent.left != None:
        #     parent.left.parent = parent
        parent.right = BuildTree(dataSet[median + 1:], depth + 1)  # (median +1) to right
        # if parent.right != None:
        #     parent.right.parent = parent
        return parent


def traversalTreeInPreOrder(root, path):
    results = []
    return traversalTreeInPreOrderHelper(root, path, results)


def traversalTreeInPreOrderHelper(root, path, results):  # preOrder recursive
    if root is None:
        return results
    # showNode()
    traversalTreeInPreOrderHelper(root.left, path + "L", results)
    traversalTreeInPreOrderHelper(root.right, path + "R", results)
    if (root.left is None) & (root.right is None):
        results.append(path)
        # showLeaf(root, path)
        leaves[path] = root.__dict__["nodes"]
    return results


def getBoundingValue(dataSets):
    # calculate Bounding value
    # dataSets = root.nodes
    # print(dataSets)
    minBounding = []
    maxBounding = []
    for d in range(dimensionType):
        minBounding.append(findMin(dataSets, d))
        maxBounding.append(findMax(dataSets, d))
    # print("Bounding Box : ", minBounding , " , ", maxBounding)
    answer = []
    answer.append(minBounding)
    answer.append(maxBounding)
    return answer


def findMin(dataSet, dimension):
    min = 1.0
    for s in dataSet:
        if s[dimension] < min:
            min = s[dimension]
    return min


def findMax(dataSet, dimension):
    max = 0.0
    for s in dataSet:
        if s[dimension] > max:
            max = s[dimension]
    return max


class TreeNode:
    def __init__(self, nodes=None, left=None, right=None, parent=None):
        self.nodes = nodes
        # self.split = split
        self.left = left
        self.right = right
        self.parent = parent


def showNode(root):
    print('items:', '\n '.join(['%s:%s' % item for item in root.__dict__.items()]))
    print()


def showLeaf(root, path):
    print(path, " : ", root.__dict__["nodes"])
    print()


if __name__ == "__main__":
    getInputs()
