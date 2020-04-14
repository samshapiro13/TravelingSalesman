# Sam Shapiro and Kenedy Thorne
# CS 3510 Final Project

import sys, math, random

# Setup all command line arguments, clear output file
inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'a')
outputFile.truncate(0)
timeLimit = sys.argv[3]

nodes = []

# Read input file into nodes as 2D array
for line in inputFile:
    fields = line.split(" ")
    fields[2] = fields[2][0:len(fields[2])-2]
    mapFields = map(float, fields)
    nodes.append(mapFields)

# Finds cartesian distance between 2 points
def distance(x1, y1, x2, y2):
    return int(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))


#----------------------------------------------------------#
# CHOOSE NEW ALGORITHM
# STILL NEED TO IMPLEMENT TIMEOUT FUNCTIONALITY


# Nearest neighbor algorithm with 10 random starting nodes
paths = [[0 for q in range(29)] for p in range(0)]
for r in range(10):
    randStart = random.randint(1, 29)

    path = [len(nodes)]
    path[0] = randStart
    tourLength = 0
    for i in range(len(nodes)-1):
        minDistance = sys.maxsize
        nextNode = path[0]
        for j in range(len(nodes)):
            nodeNumber = int(nodes[j][0])
            if nodeNumber not in path:
                dist = distance(nodes[path[i] - 1][1], nodes[path[i] - 1][2], nodes[j][1], nodes[j][2])
                if (dist < minDistance):
                    minDistance = dist
                    nextNode = nodeNumber
        tourLength = tourLength + minDistance
        path.append(nextNode)

    finalDistance = distance(nodes[path[len(nodes)-1]-1][1], nodes[path[len(nodes)-1]-1][2], nodes[randStart-1][1], nodes[randStart-1][2])
    tourLength = tourLength + finalDistance
    path.append(randStart)
    path.append(tourLength)
    paths.append(path)

# Find average tour length
sumTour = 0
for g in range(10):
    sumTour = sumTour + paths[g][30]
avgTour = sumTour/10

# Write to outpur file
outputFile.write(str(avgTour))
outputFile.write("\n")
for k in range(10):
    for h in range(len(paths[k]) - 1):
        outputFile.write(str(paths[k][h]) + " ")
    outputFile.write("\n")