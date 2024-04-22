import csv

from BlockData import BlockData

textMap = []
for j in [[BlockData() for _ in range(10)] for _ in range(10)]:
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

    
with open('hazards.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(["Team Number: 21", "Map Number: " + str(0), "Notes: this is an example map"])
    spamwriter.writerows(textMap)