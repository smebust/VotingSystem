import tkinter as tk
from tkinter import *
import ballot as blt
import popUp as pUp


#-------------------------------------------------------------------------------------------------------------------
# Voter class acts as instances of voter, each one containing simple data about voter info and preferences
#
#-------------------------------------------------------------------------------------------------------------------

class Voter:
    def __init__(self, prefDict, name, eType):
        self.prefDict = prefDict
        self.name = name
        self.eType = eType
        self.vote = self.getFav()

    #-------------------------------------------------------------------------------------------------------
    # resetVote(): used to change where this voter instance's vote goes
    # changes vote to next preference, called when voter's current choice is eliminated
    #-------------------------------------------------------------------------------------------------------

    def resetVote(self):
        #int representing rank of current vote
        print("vrank: " + str(self.prefDict[self.vote]))
        vrank = int(self.prefDict[self.vote])
        vrank += 1
        #looks for key in preference dictionary corresponding to the next highest ranking preference
        for key in self.prefDict.keys():
            if (int(self.prefDict[key]) == vrank):
                #print("MADE IT!!!!!!")
                self.vote = key
                return

    #-------------------------------------------------------------------------------------------------------
    # getPref(): Takes a key and returns the stored preference values for given key
    #-------------------------------------------------------------------------------------------------------

    def getPref(self, nameStr):
        return self.prefDict[nameStr]

    #-------------------------------------------------------------------------------------------------------
    # getPrefs(): Returns the prefDict data memeber containing a list of names and associated preferences
    #-------------------------------------------------------------------------------------------------------

    def getPrefs(self):
        return self.prefDict

    #-------------------------------------------------------------------------------------------------------
    # getFav(): returns the highest ranked choice for given voter
    #-------------------------------------------------------------------------------------------------------

    def getFav(self):
        if(self.eType == "Ranked-Choice"):
            for key in self.prefDict.keys():
                if self.prefDict[key] == '1':
                    return key
        elif(self.eType == "Scaled-Rating"):
            fav = 0
            for key in self.prefDict.keys():
                if (self.prefDict[key] > fav):
                    fav = self.prefDict[key]
            return fav

    #-------------------------------------------------------------------------------------------------------
    # getVote(): getter, returns current vote for given voter
    #-------------------------------------------------------------------------------------------------------

    def getVote(self):
        return self.vote

    #-------------------------------------------------------------------------------------------------------
    # getName(): getter, returns current name for given voter
    #-------------------------------------------------------------------------------------------------------
  
    def getName(self):
        return self.name

    #-------------------------------------------------------------------------------------------------------
    # getOrderedPrefs(): INCOMPLETE - return list of candidates recieving prefs from given voter in order
    #-------------------------------------------------------------------------------------------------------

    def getOrderedPrefs(self):
        if (self.etype == "Ranked-Choice"):
            pass
        elif (self.etype == "Scaled-Rating"):
            pass

    #-------------------------------------------------------------------------------------------------------
    # __str__(): string method, prints voter name then prefDict
    #-------------------------------------------------------------------------------------------------------

    def __str__(self):
        toRet = self.name + "'s Rankings: "
        count = 1
        for key in self.prefDict.keys():
            toRet += str(key)
            toRet += ": "
            toRet += str(self.prefDict[key])
            if(count != len(self.prefDict.keys())): 
                toRet += ", "
            count+=1

        return toRet

