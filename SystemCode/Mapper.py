import time
import math
import csv

from BlockData import BlockData

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
        self.map = [[BlockData() for _ in range(width)] for _ in range(height)] 
        self.mapNumber = mapNumber
        self.hazardList = [["Hazard Type", "Parameter of Interest", "Parameter Value", "Hazard X Coordinate (cm)", "Hazard Y Coordinate (cm)"]]

    # set inital position in cm
    def initOrgin(self, x, y):
        self.xOrigin = x
        self.yOrigin = y

    #update map and hazard list
    def update(self, x,y, isIR=False, isMag=False, irValue=None, magValue=None):
        blockX = math.floor((x) / self.blockSize) + self.xOrigin
        blockY = math.floor((y) / self.blockSize) + self.yOrigin
        currBlock = self.map[blockY][blockX]
    # updates map
        currBlock.isBeen = True
        if currBlock == True or isIR:
            currBlock.isIR = True
    # update hazard list
            flag = True
            for hazard in self.hazardList:
                if hazard[3] == blockX and hazard[4] == blockY:
                    flag = False
            if flag:
                self.hazardList.append(["High Temperature Heat Source", "Radiated Power (W)", irValue, x, y])
    # updates map
        if currBlock.isMag == True or isMag:
            currBlock.setMag(True)
    # update hazard list
            flag = True
            for hazard in self.hazardList:
                if hazard[3] != blockX and hazard[4] != blockY:
                    flag = False
            if flag:
                self.hazardList.append(["Electrical/Magnetic Activity Source", "Field strength (uT)", magValue, x, y])
    # put changes into map
        self.map[blockY][blockX] = currBlock

    # add end block
    def addEndBlock(self, blockX: int, blockY: int):
        points = self.map[blockY][blockX]
        points.setEnd(True)
        self.map[blockY][blockX] = points

    def getMap(self):
        textMap = ""
        for j in self.map:
            row = ""
            for i in j:
                point = "0"
                if i.isBeen == True:
                    point = "1"
                row += point + " | "
            textMap += row + "\n"

        textMap.reverse()
        return textMap
    
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