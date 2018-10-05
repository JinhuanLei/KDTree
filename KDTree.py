import sys
import os
module_path = os.path.dirname(__file__)
def GetInputs():
    fileName=sys.argv[1]
    minSize=sys.argv[2]
    print(fileName+" "+minSize)
    # print(os.getcwd())
    # print(module_path)


if __name__=="__main__":
	GetInputs()
