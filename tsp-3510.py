# Sam Shapiro and Kenedy Thorne
# CS 3510 Final Project

import sys

# Setup all command line arguments, clear output file
inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'a')
outputFile.truncate(0)
timeLimit = sys.argv[3]

nodes = []

# Read input file into nodes as 2D array
for line in inputFile:
    fields = line.split(" ")
    fields[2] = fields[2][0:len(fields[2])-1]
    nodes.append(fields)


outputFile.write("Hello ")
print(nodes)