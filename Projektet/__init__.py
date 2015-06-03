import sqlite3
import datetime
from tkinter import *

db = sqlite3.connect('KEAbib.db')
c = db.cursor()

def udlaan(bNavn, did):
    bid = c.execute("SELECT brugerid FROM Bruger WHERE navn = ?", [bNavn]).fetchall()
    bid = bid[0][0]
    now = datetime.datetime.now()
    try:
        c.execute("INSERT INTO Loan(bid, did, loan) VALUES (?, ?, ?)", (str(bid), str(did), now))
        db.commit()
    except:
        db.rollback()
    return

def deviceErUdlaant(did):
    checker = c.execute('SELECT * FROM Loan WHERE (did = ?)', [did]).fetchall()
    checker2 = c.execute('SELECT * FROM Loan WHERE (did = ? AND delivered NOT NULL)', [did]).fetchall()
    if (len(checker) >= 1):
        if (len(checker2) >= len(checker)):
            isRented = False
        else:
            isRented = True
    else:
        isRented = False
    return isRented

def afflevering(bNavn, did):
    bid = c.execute("SELECT brugerid FROM Bruger WHERE navn = ?", [bNavn]).fetchall()
    bid = bid[0][0]
    now = datetime.datetime.now()
    try:
        c.execute("UPDATE Loan SET delivered = ? WHERE bid = ? AND did = ?", (now, str(bid), str(did)))
        db.commit()
    except:
        db.rollback()
    return

def muligAff(bNavn, did):
    bid = c.execute("SELECT brugerid FROM Bruger WHERE navn = ?", [bNavn]).fetchall()
    bid = bid[0][0]
    mulige = c.execute("Select * From Loan Where bid = ? AND did = ? AND delivered IS NULL", (str(bid), str(did))).fetchall()
    if len(mulige) >= 1:
        possible = True
    else:
        possible = False
    return possible

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.instruction1 = Label(self, text = "KEA ID: ")
        self.instruction1.grid(row = 0, column = 0, columnspan = 1, sticky = W)
        
        self.BrugerIDEntry = Entry(self)
        self.BrugerIDEntry.grid(row = 0, column = 1, sticky = W)
        
        self.instruction2 = Label(self, text = "Computer ID: ")
        self.instruction2.grid(row = 0, column = 2, columnspan = 1, sticky = W)
        
        self.ComputerIDEntry = Entry(self)
        self.ComputerIDEntry.grid(row = 0, column = 3, sticky = W)
        
        self.text = Text(self, width = 60, height = 5, wrap = WORD)
        self.text.grid(row = 1, column = 0, columnspan = 5, sticky = W)
        
        self.LoanButton = Button(self, text = "Laan Computer", command = self.udlaaner)
        self.LoanButton.grid(row = 2, column = 1, sticky = W)
        
        self.ReturnButton = Button(self, text = "Afflever Compueter", command = self.affleverCom)
        self.ReturnButton.grid(row = 2, column = 3, sticky = W)
        
    def somthing(self):
        self.content = "Hello"
        print (c.execute("Select deviceid From Device").fetchall())
        print (c.execute("Select * From Loan").fetchall())
        print (c.execute("Select deviceid From Device Where deviceid NOT IN (Select did From Loan)").fetchall())
    
    def udlaaner(self):
        brugerID = self.BrugerIDEntry.get()
        computerID = self.ComputerIDEntry.get()
        if (len(computerID) >= 1) and (len(brugerID) >= 1):
            if deviceErUdlaant(computerID):
                message = "Computeren er udlaant, kan ikke laanes"
            else:
                udlaan(brugerID, computerID)
                message = "Computer " + computerID + " er nu udlaant til: " + brugerID
            self.text.delete(0.0, END)
            self.text.insert(0.0, message)
    
    def affleverCom(self):
        brugerID = self.BrugerIDEntry.get()
        computerID = self.ComputerIDEntry.get()
        if (len(brugerID) >= 1) and (len(computerID) >= 1):
            if muligAff(brugerID, computerID):
                afflevering(brugerID, computerID)
                message = brugerID + " har nu affleveret computer: " + computerID
            else:
                message = "Der er ingen computere der er laant af denne person"
            self.text.delete(0.0, END)
            self.text.insert(0.0, message)


root = Tk()
root.title("Computer Udlaan og Afflevering")
root.geometry("500x135")
app = Application(root)

root.mainloop()