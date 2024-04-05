import time
import math

class Mapper():
    width = None
    height = None
    map = None
    xOffset = None
    blockSize = None

    def __init__(self, width, height, blockSize):
        self.blockSize = blockSize
        self.width = width
        self.height = height
        self.map = [[{"Marked": False, "isIR": False, "isMag": False}] * width] * height
        self.xOffset = math.ceil(width / 2)

    def update(self, x,y, isIR=False, isMag=False):
        blockX = math.floor(x / self.blockSize + self.xOffset)
        blockY = math.floor(y / self.blockSize)

        currBlock = self.map[blockX][blockY]
        irVal = True if currBlock["isIR"] or isIR else False
        magVal = True if currBlock["isMag"] or isMag else False
        self.map[blockX][blockY] = {"Marked": True, "isIR": irVal, "isMag": magVal}

    def returnMap(self):
        return self.map