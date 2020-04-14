# Sam Shapiro and Kenedy Thorne
# CS 3510 Final Project

import sys, math

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

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

dist = distance(nodes[0][1], nodes[0][2], nodes[1][1], nodes[1][2])

outputFile.write("Hello ")
print(dist)
print("\n")
print(nodes)