import sqlite3
import datetime
import os
from tkinter import *

db = sqlite3.connect('KEAbib.db')
c = db.cursor()


class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        
        self.text = Text(self, width = 60, height = 25, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 10, sticky = W)
        
        self.ShowButton = Button(self, text = "Tilfoj ny person", command = self.newper)
        self.ShowButton.grid(row = 1, column = 0, sticky = W)
        
        self.ShowButton = Button(self, text = "Tilfoj ny computer", command = self.nyCom)
        self.ShowButton.grid(row = 1, column = 1, sticky = W)
        
        self.ShowButton = Button(self, text = "Udlaan og aflevering", command = self.laaner)
        self.ShowButton.grid(row = 1, column = 2, sticky = W)
        
        self.showButton = Button(self, text = "Vis alle brugere", command = self.showing)
        self.showButton.grid(row = 1, column = 3, sticky = W)
        
        self.ShowButton = Button(self, text = "Vis alle ledige", command = self.visLedige)
        self.ShowButton.grid(row = 2, column = 0, sticky = W)
        
        self.ShowAllButton = Button(self, text = "Vis alle laante", command = self.vislaante)
        self.ShowAllButton.grid(row = 2, column = 1, sticky = W)
        
        self.ShowOldButton = Button(self, text = "Vis alle udlaante", command = self.visGammle)
        self.ShowOldButton.grid(row = 2, column = 2, sticky = W)
        
        self.showButton = Button(self, text = "Vis alle computere", command = self.showingD)
        self.showButton.grid(row = 2, column = 3, sticky = W)
        
        
        
    def newper(self):
        os.startfile("run nyPerson.bat")
        
    def nyCom(self):
        os.startfile("run newCom.bat")
        
    def laaner(self):
        os.startfile("run udlaan.bat")
        
    
    def showing(self):
        alleBrugere = c.execute("Select * From Bruger").fetchall()
        self.text.delete(0.0, END)
        for i in alleBrugere:
            self.text.insert(0.0, str(i) + "\n")
    
    def showingD(self):
        alleBrugere = c.execute("Select * From Device").fetchall()
        self.text.delete(0.0, END)
        for i in alleBrugere:
            self.text.insert(0.0, str(i) + "\n")
    
    def visLedige(self):
        midlertidig = c.execute("Select * From Device Where deviceid NOT IN (Select did From Loan Where delivered IS NULL)").fetchall()
        self.text.delete(0.0, END)
        for i in midlertidig:
            self.text.insert(0.0, str(i) + "\n")
            
    def visGammle(self):
        midlertidig = c.execute("Select * From Loan Where delivered IS NOT NULL").fetchall()
        self.text.delete(0.0, END)
        for i in midlertidig:
            self.text.insert(0.0, str(i) + "\n")        
            
    def vislaante(self):
        midlertidig = c.execute("Select * From Device Where deviceid IN (Select did From Loan Where delivered IS NULL)").fetchall()
        self.text.delete(0.0, END)
        for i in midlertidig:
            self.text.insert(0.0, str(i) + "\n")
        
        
root = Tk()
root.title("Main GUI")
root.geometry("500x475")
app = Application(root)

root.mainloop()
