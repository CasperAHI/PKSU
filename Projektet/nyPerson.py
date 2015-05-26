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
        self.instruction1 = Label(self, text = "mail: ")
        self.instruction1.grid(row = 0, column = 1, columnspan = 1, sticky = W)
        
        self.mailEntry = Entry(self)
        self.mailEntry.grid(row = 0, column = 2, sticky = W)
        
        self.instruction2 = Label(self, text = "KEA ID: ")
        self.instruction2.grid(row = 0, column = 3, columnspan = 1, sticky = W)
        
        self.KeaIDEntry = Entry(self)
        self.KeaIDEntry.grid(row = 0, column = 4, sticky = W)
        
        self.instruction2 = Label(self, text = "Telefon nr: ")
        self.instruction2.grid(row = 0, column = 5, columnspan = 1, sticky = W)
        
        self.phoneEntry = Entry(self)
        self.phoneEntry.grid(row = 0, column = 6, sticky = W)
        
        self.text = Text(self, width = 60, height = 30, wrap = WORD)
        self.text.grid(row = 1, column = 2, columnspan = 10, sticky = W)
        
        self.AddComButton = Button(self, text = "Tilfoj ny person", command = self.somthing)
        self.AddComButton.grid(row = 2, column = 2, sticky = W)
        
    def somthing(self):
        mail = self.mailEntry.get()
        navn = self.KeaIDEntry.get()
        telefon = self.phoneEntry.get()
        if (len(mail) >= 1) and (len(navn) >= 1) and (len(telefon) >= 1):
            checker = c.execute("Select * From Bruger Where mail = ? AND navn = ? AND telefon = ?", (mail, navn, telefon)).fetchall()
            if len(checker) == 0:
                c.execute("INSERT INTO Bruger(mail, navn, telefon) VALUES (?, ?, ?)", (mail, navn, telefon))
                db.commit()
                message = "En ny bruger er blevet tilfojet til systemet"
            else:
                message = "Denne bruger er allerede i systemet"
            self.text.delete(0.0, END)
            self.text.insert(0.0, message)
    
    
root = Tk()
root.title("Tilfoj ny bruger")
root.geometry("550x550")
app = Application(root)

root.mainloop()