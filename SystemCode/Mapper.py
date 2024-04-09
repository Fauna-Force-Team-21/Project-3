import time
import math
import csv

class Mapper():
    width = None
    height = None
    map = None
    xOrigin = None
    yOrigin = None
    blockSize = None
    mapNumber = None
    hazardList = None

    def __init__(self, width, height, blockSize, mapNumber):
        self.blockSize = blockSize
        self.width = width
        self.height = height
        self.map = [[0] * width] * height
        self.mapNumber = mapNumber
        self.hazardList = [["Hazard Type", "Parameter of Interest", "Parameter Value", "Hazard X Coordinate (cm)", "Hazard Y Coordinate (cm)"]]

    # set inital position in cm
    def initOrgin(self, x, y):
        self.xOrigin = x
        self.yOrigin = y

    #update map and hazard list
    def update(self, x,y, isIR=False, isMag=False, irValue=None, magValue=None):
        blockX = math.floor((x) / self.blockSize)
        blockY = math.floor((y) / self.blockSize)

        currBlock = self.map[blockX][blockY]
    # updates map
        blockVal = 5 if blockX == self.xOrigin and blockY == self.yOrigin else 1
        if currBlock  == 2 or isIR:
            blockVal = 2
    # update hazard list
            for hazard in self.hazardList:
                if hazard[3] != blockX and hazard[4] != blockY:
                    self.hazardList.append(["High Temperature Heat Source", "Radiated Power (W)", irValue, x, y])
    # updates map
        if currBlock == 3 or isMag:
            blockVal = 3
    # update hazard list
            for hazard in self.hazardList:
                if hazard[3] != blockX and hazard[4] != blockY:
                    self.hazardList.append(["Electrical/Magnetic Activity Source", "Field strength (uT)", magValue, x, y])
    # put changes into map
        self.map[blockX][blockY] = blockVal

    # add end block
    def addEndBlock(self, blockX, blockY):
        self.map[blockX][blockY] = 4

    def returnMap(self):
        return self.map
    
    # prints map to a csv file
    def printMap(self):
        with open('map.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(["Team Number: 21", "Map Number: " + str(self.mapNumber), "Unit Length: " + str(self.blockSize), "Unit: cm", "Orgin: (" + str(self.xOrigin / self.blockSize) + ", " + str(self.yOrigin / self.blockSize) + ")", "Notes: this is an example map"])
            spamwriter.writerows(self.map)

    # prints map to csv file
    def printHazards(self):
        with open('hazards.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(["Team Number: 21", "Map Number: " + str(self.mapNumber), "Notes: this is an example map"])
            spamwriter.writerows(self.hazardList)