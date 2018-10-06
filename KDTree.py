import sys
import os
def getInputs():
    arguments = sys.argv
    if len(arguments) != 3:
        print("Please Enter Correct Inputs !")
        return
    fileName = sys.argv[1]
    minSize = sys.argv[2]
    # print(os.path.exists(module_path+"2d_large.txt"))
    # print(module_path+"/"+fileName)
    module_path = os.path.dirname(__file__)
    dataFile = module_path + fileName
    if not os.path.exists(dataFile):
        print("Please Enter Correct File name !")
        return
    inputData = []
    with open(dataFile, "r") as f:
        # data=f.readlines()
        for line in f.readlines():
            line = line.strip()
            inputData.append(list(map(str, line.split(" "))))
    dimentionType = inputData[0]
    dataSet = inputData[1:]
    print(dimentionType)
    # print(dataSet)
    BuildTree(dataSet,dimentionType,minSize)


def BuildTree(dataSet,dimentionType,minSize):
    pass



if __name__ == "__main__":
    getInputs()
