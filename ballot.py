import tkinter as tk
from tkinter import *

import popUp as pUp
import voter as vtr

#-------------------------------------------------------------------------------------------------------------------
# Ballot class handles voter data input, runs election scripts and outputs winner
#
#-------------------------------------------------------------------------------------------------------------------
class Ballot:
    def __init__(self, names, etype):
        self.names = names
        self.wlist = []
        self.etype = etype
        self.voters = []
        self.ballot = pUp.popUp()

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def make_ballot(self):

        for i in range(len(self.names) + 1):
            if (i == 0):
                self.ballot.addLabel(text = "Enter Name: ")
                self.ballot.addEntry()
            else:
                use = self.names[i-1] + ": "
                self.ballot.addLabel(text = use)
                if (self.etype == "Ranked-Choice"):
                    self.ballot.addEntry()
                elif (self.etype == "Scaled-Rating"):
                    self.ballot.addScale(0, 100)

        if (self.etype == "Ranked-Choice"):
            self.ballot.addButton(text = "Push to Save Entries", command = self.saveRanks)
        elif(self.etype == "Scaled-Rating"):
            self.ballot.addButton(text = "Push to Save Ratings", command = self.saveRatings)
            
        self.ballot.addButton(text = "Push to Show Results", command = self.runElection)
        self.ballot.addButton(text = "Push to Run Voter Report", command = self.genRep)
        self.ballot.run()

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    #Generate Report: this method makes use of global list 'voters[]' 
    #Creates a tkinter frame that acts as a pop-up window which lists each voter, along with their ordered preferences 
    def genRep(self):
        repBox = pUp.popUp()
        for i in self.voters:
            repBox.addLabel(text = str(i))
        repBox.run()
    
    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def saveRatings(self):
        prefDict = {}
        rates = []
        #get rates from scales
        for i in self.ballot.sVars:
            rates.append(i.get())
        print(rates)
        for i in range(len(self.names)):
            prefDict[self.names[i]] = rates[i]

        voter = self.ballot.eList[0].get()
        #print(voter)
        ballot_entry = vtr.Voter(prefDict, voter, self.etype)
        self.voters.append(ballot_entry)
        saved = pUp.popUp()
        saved.addLabel(text = "Your Ratings Have Been Saved!")
        saved.run()
            
    #-------------------------------------------------------------------------------------------------------
    #below function serves to save the current entries as an instance of the Voter class
    #-------------------------------------------------------------------------------------------------------

    def saveRanks(self):
        prefDict = {}
        ranks = []
        #gets values from entry boxes
        for i in range(len(self.ballot.eList)):
            if i != 0:
                ranks.append(self.ballot.eList[i].get())
        legal = []
        for i in range(len(self.names)):
            legal.append(i+1)

        legalRanks = []
        #handles case of input not equal to integer ranks
        for i in ranks:
            if(i == ''):
                pass
            elif (int(i) in legal) != True:
                errBox = pUp.popUp()
                errBox.addLabel(text = "ERROR: Please rank using only the values: " + ', '.join(str(e) for e in legal))
                errBox.run()
                exit()
            else:
                legalRanks.append(i)

        #handles case of any two candidates ranked equally
        if len(legalRanks) > len(set(legalRanks)):

            errBox = pUp.popUp()
            errBox.addLabel(text = "ERROR: Do not give multiple candidates the same rank")
            errBox.run()
            exit()   

            

        for i in range(len(self.names)):
            prefDict[self.names[i]] = ranks[i]

        voter = self.ballot.eList[0].get()
        #print(voter)
        ballot_entry = vtr.Voter(prefDict, voter, self.etype)
        self.voters.append(ballot_entry)
        saved = pUp.popUp()
        saved.addLabel(text = "Your Ranks Have Been Saved")
        saved.run()

        

    #-------------------------------------------------------------------------------------------------------
    #show() method creates a dictionary, keys being names and values being a list of the ranking of the
    #corresponding name from each voter.
    #-------------------------------------------------------------------------------------------------------

    def show(self):
        resultDict = {}
        for i in self.names:
            resultDict[i] = []
        for i in self.voters:
            for j in self.names:
                resultDict[j].append(i.getPref(j))
        
        print(resultDict)

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def winner(self, wName):
        foundWinner = True
        wpop = pUp.popUp()
        wpop.addLabel(text = wName + " wins!")
        wpop.run()
        exit()

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def rankCElect(self):
        #get votes from voters list
        fChoice = self.getVotes()
        print(' '.join(fChoice))

        

        #Dictionary containing only candidates who received votes as keys, along with vote count as values
        elDict = {}

        for i in self.names:
            count = 0
            for j in fChoice:
                if j == i:
                    count+=1

            if count != 0:
                elDict[i] = count
        #checks first for winner, ends if one is found. if not, changes votes and tries again
        for key in elDict.keys():
            if elDict[key] > (len(self.voters)/2):
                self.winner(key)
                return
            else:
                self.changeVotes(elDict)
                self.rankCElect()        

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------
    def ratingElect(self):
        allRDict = {}
        for name in self.names:
            allRDict[name] = 0
        print("allRDict: \n")
        print(allRDict)

        for voter in self.voters:
            print("Voter: ")
            print(voter.name)
            print("\nVoterPrefs:\n")
            print(voter.getPrefs())
            dictToAdd = {}
            for key in (voter.getPrefs().keys()):
                val = int(voter.getPrefs()[key])
                dictToAdd[key] = val
            print(dictToAdd)
            for key in dictToAdd.keys():
                k = str(key)
                allRDict[key] += dictToAdd[key]

        winnerR = 0
        winner = ""
        for key in allRDict.keys():
            if (allRDict[key] > winnerR):
                winnerR = allRDict[key]
                winner = key
        self.winner(winner)
            
        


    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------
    
    def runElection(self):
        if (self.etype == "Ranked-Choice"):
            self.rankCElect()
        elif (self.etype == "Scaled-Rating"):
            self.ratingElect()
        
        
    #-------------------------------------------------------------------------------------------------------
    #Performs reordering operation on voter list
    #Used in ranked choice voting system
    #-------------------------------------------------------------------------------------------------------

    def changeVotes(self, elDict):
        ldr = ""
        ldrcount = 0
        lsr = ""
        lsrcount = 2147483648

        #find current leader (most votes)
        for key in elDict.keys():
            if int(elDict[key]) > ldrcount:
                ldrcount = int(elDict[key])
                ldr = str(key)

        #find candidate with least votes
        for key in elDict.keys():
            if int(elDict[key]) < lsrcount:
                lsrcount = int(elDict[key])
                lsr = str(key)

        #changes votes of voters who's current vote is going to the candidate with least support
        for vtr in self.voters:
            if (vtr.getVote() == lsr):
                #print(vtr.getName())
                #print(vtr.getVote())
                #changes voter vote to next highest pref
                vtr.resetVote()

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def getVotes(self):
        fChoice = []
        for i in self.voters:
            fave = i.getVote()
            fChoice.append(fave)

        return fChoice
