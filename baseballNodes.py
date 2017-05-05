"""
William Dreese 2017
Developement

Basic UI for handling the data and testing it for Baseball Nodes.
"""

from nodeBayes import nodeBayes
from nodeGeneral import Node, teamDict
from rawToNode import rawToNode

def interface(nB):
    a = "T"
    while a != "X":
        print("Baseball Nodes")
        print("[T] Test a team against current data (Phillies)")
        print("[U] Update the Data with a csv file")
        print("[X] Quit")
        a = input("")
        if a == "T":
            tester(nB)
        print("")

def tester(nB):
    team = input("Opponent (PHI, MIA, CHC, etc.): ")

    div = input("Opponent in division (Y/N): ")
    if div == "Y": div = 1
    else: div = 0

    ha = input("Home or Away (H/A): ")
    if ha == "H": ha = 1
    else: ha = 0

    dn = input("Day or Night (D/N): ")
    if dn == "D": dn = 1
    else: dn = 0

    nB.test(team,div,ha,dn)

rTN = rawToNode(["rawData.txt"])
rTN.runFile(0)
nB = nodeBayes(rTN._nodes)
interface(nB)
