"""
2017 William Dreese
Developement
Stores all Node-related classes, scales, and lists.
Need to define stuff for pitching related later, also streak stuff

attribute/integer (teams in teamDict)
Home 1  Win  1 Day   1 InDiv  1
Away 0  Loss 0 Night 0 OutDiv 0
"""

TEAMS = [["NL East","PHI","ATL","NYM","MIA","WSN"],
         ["NL Central","MIL","CHC","CIN","STL","PIT"],
         ["NL West","ARI","COL","SFG","LAD","SDP"],
         ["AL East","NYY","TBR","TOR","BAL","BOS"],
         ["AL Central","MIN","CHW","CLE","DET","KCR"],
         ["AL West","LAA","TEX","OAK","HOU","SEA"]]

teamDict = {}

class Node:
                   
    #Node = a game of baseball
    def __init__(self, line):
        num = 0
        for div in TEAMS:
            for i in range(1,6):
                teamDict[div[i]] = num
                num += 1
        #attList (in order) = oppo, div, h/a, d/n, win
        #make sure node is refined before analysis
        
        self._gameNum = line[0]
        self._date = line[1]
        self._team = line[3]
        self._opponent = line[5]
        
        ha = 1
        if line[4] == "@": ha = 0
        self._homeAway = ha
        
        self._win = line[6][0]
        if self._win == "W": self._win = 1
        else: self._win = 0
        
        self._runsScored = int(line[7])
        self._runsAllowed = int(line[8])
        
        extras = 0
        if line[9] != "": extras = 1
        self._extras = extras
        
        self._winPit = line[13]
        self._losPit = line[14]
        
        self._dayNight = line[17][0]
        if self._dayNight == "D": self._dayNight = 1
        else: self._dayNight = 0
        
        self._streak = line[19]
        self._div = 0
        for di in TEAMS:
            if self._team in di and self._opponent in di: self._div = 1

        self._attributes = [teamDict[self._opponent],
                            self._div,
                            self._homeAway,
                            self._dayNight,
                            self._win]

    def __str__(self):
        a = ""
        for b in self._attributes: a += str(b) + ","
        return a
        
    def toCSV(self):
        #returns a refined CSV line for storage
        return self._gameNum
