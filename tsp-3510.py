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
# STILL NEED TO IMPLEMENT TIMEOUT FUNCTIONALITY


# Create initial tour in order of appearance starting at node 1
path = []
tourLength = 0
for i in range(len(nodes)):
    path.append(int(nodes[i][0]))
for j in range(len(path)-1):
    dist = distance(nodes[path[j] - 1][1], nodes[path[j] - 1][2], nodes[path[j]][1], nodes[path[j]][2])
    tourLength = tourLength + dist

# Add first node to end of path
finalDistance = distance(nodes[len(nodes)-1][1], nodes[len(nodes)-1][2], nodes[0][1], nodes[0][2])
tourLength = tourLength + finalDistance
path.append(1)

#----------------------------------------------------------#
# BEGIN 2-OPT FUNCTIONALITY




# Write to output file
outputFile.write(str(tourLength))
outputFile.write("\n")
for h in range(len(path)):
    outputFile.write(str(path[h]) + " ")