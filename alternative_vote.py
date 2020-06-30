import tkinter as tk
from tkinter import *

import ballot as blt
import popUp as pUp
import voter as vtr

#-------------------------------------------------------------------------------------------------------
# Master script used to run election
#-------------------------------------------------------------------------------------------------------

def setup():
    #print("Enter Names: ")
    options = open("names.txt", "rt")
    nameString = options.read()
    namesL = nameString.split("\n")
    names = []
    for i in namesL:
        names.append(i)

    return names

def main():
    eType = "Scaled-Rating"
    names = setup()
    ballot = blt.Ballot(names, eType)
    ballot.make_ballot()

if __name__ == "__main__": main()



