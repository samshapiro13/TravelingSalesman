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

# Find tour length of any given path
def findTourLength(tour):
    thisTourLength = 0
    for x in range(len(tour)):
        thisTourLength = thisTourLength + distances[tour[x-1] - 1][tour[x] - 1]
    return thisTourLength

# Create 2D array of distances between each node
distances = [[0 for x in range(len(nodes))] for y in range(len(nodes))]
for p in range(len(nodes)):
    for q in range(len(nodes)):
        distances[p][q] = distance(nodes[p][1], nodes[p][2], nodes[q][1], nodes[q][2])


#----------------------------------------------------------#
# STILL NEED TO IMPLEMENT TIMEOUT FUNCTIONALITY


# Create initial tour in order of appearance starting at node 1
path = []
tourLength = 0
for i in range(len(nodes)):
    path.append(int(nodes[i][0]))
for j in range(len(path)-1):
    dist = distances[path[j] - 1][path[j]]
    tourLength = tourLength + dist

# Add first node to end of path
finalDistance = distances[len(nodes)-1][0]
tourLength = tourLength + finalDistance
path.append(1)

#----------------------------------------------------------#
# BEGIN 2-OPT FUNCTIONALITY

# Function to swap path between 2 nodes in the tour
def swapInPath(tour, a, b):
    arr = [len(tour)]
    arr = tour[0:a]
    arr.extend(reversed(tour[a:b + 1]))
    arr.extend(tour[b + 1:])
    return arr

# Function to run 2-OPT until no more improvements are found
def run2OPT(tour):
    foundImprovement = True
    bestTour = tour
    bestTourLength = findTourLength(tour)
    while foundImprovement:
        foundImprovement = False
        for f in range(len(bestTour) - 1):
            for g in range(f + 1, len(bestTour)):
                newTour = swapInPath(bestTour, f, g)
                newTourLength = findTourLength(newTour)
                if newTourLength < bestTourLength:
                    bestTourLength = newTourLength
                    bestTour = newTour
                    foundImprovement = True
                    break
            if foundImprovement:
                break
    return bestTour

finalTour = run2OPT(path)
finalTourLength = findTourLength(finalTour)

# Write to output file
outputFile.write(str(finalTourLength))
outputFile.write("\n")
for h in range(len(finalTour)):
    outputFile.write(str(finalTour[h]) + " ")