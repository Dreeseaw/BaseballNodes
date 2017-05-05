"""
William Dreese 2017
Developement

Takes a list of nodes and uses Naive Bayes machince learning
to predict test cases. Handles 1 file currently.

-add Laplace smoothing
-add pitcher analysis
-add streak analysis
"""
from nodeGeneral import Node, teamDict

class nodeBayes:

    def __init__(self, nodeList):
        self._list = nodeList
        self._l = len(self._list)
        tW = 0.0
        for node in self._list:
            tW += float(node._attributes[-1])
        self._totalProb = tW/float(self._l)

    def compileAtt(self, testVal, att):
        tmW = 0.0
        tm = 0.0
        for node in self._list:
            if node._attributes[att] == testVal:
                tmW += float(node._attributes[-1])
                tm += 1.0
        ret = tmW/tm
        return ret / float(tm/float(self._l))
                
    def test(self, oppo,div,ha,dn):
        #apply the correct compiled probs using the test case, made for baseball
        op = teamDict[oppo]
        
        ret = self._totalProb
        ret *= self.compileAtt(op,0)
        ret *= self.compileAtt(div,1)
        ret *= self.compileAtt(ha,2)
        ret *= self.compileAtt(dn,3)
        
        ret = float(int(ret*10000.0))/100.0
        print("PHI v",oppo,"win chance: %",ret)
    
