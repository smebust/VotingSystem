import tkinter as tk
from tkinter import *
import ballot as blt
import voter as vtr

#-------------------------------------------------------------------------------------------------------------------
# popUp class handles creation of tkinter windows
#creates the main ballot box window, as well as all windows created for popup messages
#-------------------------------------------------------------------------------------------------------------------

class popUp:
    def __init__(self):
        self.eList = []
        self.eVars = []
        self.bList = []
        self.lList = []
        self.sList = []
        self.sVars = []
        self.window = tk.Tk()

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def addEntry(self):
        toUse = StringVar()
        self.eList.append(Entry(self.window, textvariable = toUse))
        self.eVars.append(toUse)

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def addLabel(self, text):
        self.lList.append(Label(self.window, text = text))

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def addButton(self, text, command, arg = None):
        self.bList.append(Button(self.window, text = text, command = command))

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def addScale(self, from_, to):
        toUse = IntVar()
        self.sList.append(Scale(self.window, orient = HORIZONTAL, from_ = from_, to = to, variable = toUse))
        self.sVars.append(toUse)

    #-------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------

    def run(self):
        if (len(self.lList)>0):
            count = 0
            for label in self.lList:
                label.grid(column = 0, row = count)
                count+=1
        if (len(self.eList)>0):
            count = 0
            for entry in self.eList:
                entry.grid(column = 1, row = count)  
                count+=1 
        if (len(self.sList)>0):
            count = 1
            for scale in self.sList:
                scale.grid(column = 1, row = count)
                count +=1 
        if (len(self.bList)>0):
            count = int((len(self.lList)/2)-(len(self.bList)/2))
            for button in self.bList:
                button.grid(column = 2, row = count)
                count+=1

        self.window.mainloop()              
