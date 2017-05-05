"""
William Dreese 2017
Developement

Takes raw CSV lines and turns them into nodes (create file OR update)
Each team's current season is represented by a text files for the raw data
and refined node data. Does no real analysis. A node is one game, a list of
them then create a nodeDataFile and a new list of nodes. Those files are stored
in folders for different teams

- need to update storing nodes back into CSV
- need to work on update functions
"""
from nodeGeneral import Node

class rawToNode:
    
    def __init__(self, rawDataFiles):
        self._rDF = rawDataFiles
        self._nodes = [None]*(len(rawDataFiles))

    def refine(self, rawFile):
        #handles refining the CSV into a refined list of strings
        rW = open(rawFile,"r")
        lines = []
        for line in rW:
            line.rstrip()
            if line[0] != "G":
                if "preview" not in line:
                    lines += [line.split(",")]
        rW.close()
        return lines

    def makeNodes(self, rD):
        #turns list of refined data into list of raw nodes
        nL = []
        for line in rD:
            nL += [Node(line)]
        return nL

    def runFile(self,n):
        refinedData = self.refine(self._rDF[n])
        #get raw data, refines it
        self._nodes = self.makeNodes(refinedData)
        #put it into nodes
        return 0
