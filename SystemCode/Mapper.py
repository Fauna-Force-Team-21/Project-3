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
        currBlock = self.map[y][x]
    # updates map
        currBlock.isOrigin = True
        self.map[y][x] = currBlock

    #update map and hazard list
    def update(self, x,y, isIR=False, isMag=False, irValue=None, magValue=None):
        blockX = math.floor((x) / self.blockSize)
        blockY = math.floor((y) / self.blockSize)
        currBlock = self.map[blockY][blockX]
    # updates map
        currBlock.isBeen = True
        self.map[blockY][blockX] = currBlock
   
    # update hazard list
    def updateIR(self, value, pose2D: tuple, dist):
        xDist = dist * math.sin(pose2D[2])
        yDist = dist * math.cos(pose2D[2])
        x = pose2D[0] + xDist
        y = pose2D[1] + yDist
        blockX = math.floor((x) / self.blockSize)
        blockY = math.floor((y) / self.blockSize)
        currBlock = self.map[blockY][blockX]
    # updates map
        currBlock.isBeen = True
        currBlock.isIR = True
        self.hazardList.append(["High Temperature Heat Source", "Radiated Power (W)", value, x, y])
        self.map[blockY][blockX] = currBlock

    def updateMag(self, value, pose2D: tuple, dist):
        xDist = dist * math.sin(pose2D[2])
        yDist = dist * math.cos(pose2D[2])
        x = pose2D[0] + xDist
        y = pose2D[1] + yDist
        blockX = math.floor((x) / self.blockSize)
        blockY = math.floor((y) / self.blockSize)
        currBlock = self.map[blockY][blockX]
    # updates map
        currBlock.isBeen = True
        currBlock.isMag = True
        self.hazardList.append(["Electrical/Magnetic Activity Source", "Field strength (uT)", value, x, y])
        self.map[blockY][blockX] = currBlock

    # add end block
    def addEndBlock(self, blockX: int, blockY: int, xOffset: int, yOffset: int):
        points = self.map[blockY + yOffset][blockX + xOffset]
        points.setEnd = True
        self.map[blockY + yOffset][blockX + xOffset] = points

    def getMap(self):
        textMap = []
        for j in self.map:
            row = ""
            for i in j:
                point = "0"
                if i.isOrigin:
                    point = "5"
                elif i.isIR:
                    point = "2"
                elif i.isMag:
                    point = "3"
                elif i.isEnd:
                    point = "4"
                elif i.isBeen:
                    point = "1"
                row = row + point + " | "
            textMap.append(row)
            textMap.append("- " * len(j))

        textMap.reverse()
        finalString = ""
        for i in textMap:
            finalString += i + "\n"
        return finalString
    
    def getPrintMap(self):
        textMap = []
        for j in self.map:
            row = []
            for i in j:
                point = "0"
                if i.isOrigin:
                    point = "5"
                elif i.isIR:
                    point = "2"
                elif i.isMag:
                    point = "3"
                elif i.isEnd:
                    point = "4"
                elif i.isBeen:
                    point = "1"
                row.append(point)
            textMap.append(row)

        textMap.reverse()
        return textMap
    
    # prints map to a csv file
    def printMap(self):
        with open('map.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(["Team Number: 21", "Map Number: " + str(self.mapNumber), "Unit Length: " + str(self.blockSize), "Unit: cm", "Orgin: (" + str(self.xOrigin / self.blockSize) + ", " + str(self.yOrigin / self.blockSize) + ")", "Notes: this is an example map"])
            spamwriter.writerows(self.getPrintMap())

    # prints map to csv file
    def printHazards(self):
        with open('hazards.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(["Team Number: 21", "Map Number: " + str(self.mapNumber), "Notes: this is an example map"])
            spamwriter.writerows(self.hazardList)