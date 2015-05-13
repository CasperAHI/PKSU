import sqlite3
import datetime
from tkinter import *

db = sqlite3.connect('KEAbib.db')
c = db.cursor()


class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.ShowButton = Button(self, text = "Lav ny Database", command = self.creater)
        self.ShowButton.grid(row = 1, column = 3, sticky = W)
        
        self.text = Text(self, width = 60, height = 5, wrap = WORD)
        self.text.grid(row = 0, column = 2, columnspan = 5, sticky = W)
        
        
    def creater(self):
        message = "Databasen blev lavet hvis der ikke allerede var en"
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
        c.execute("""CREATE TABLE Bruger (
                    brugerid INTEGER PRIMARY KEY AUTOINCREMENT,
                    mail TEXT,
                    navn TEXT,
                    telefon INT )""")


        c.execute("""CREATE TABLE Device  (
                    deviceid INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT,
                    navn TEXT,
                    tyverid INT )""")

        c.execute("""CREATE TABLE Loan (
                    bid INT,
                    did INT,
                    loan DATETIME,
                    delivered DATETIME,
                    FOREIGN KEY(bid) REFERENCES Bruger(brugerid),
                    FOREIGN KEY(did) REFERENCES Device(deviceid) )""")
        


root = Tk()
root.title("Tilfoj ny bruger")
root.geometry("550x150")
app = Application(root)

root.mainloop()