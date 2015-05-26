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
        self.instruction1 = Label(self, text = "Type: ")
        self.instruction1.grid(row = 0, column = 1, columnspan = 1, sticky = W)
        
        self.DeviceTypeEntry = Entry(self)
        self.DeviceTypeEntry.grid(row = 0, column = 2, sticky = W)
        
        self.instruction2 = Label(self, text = "Device navn: ")
        self.instruction2.grid(row = 0, column = 3, columnspan = 1, sticky = W)
        
        self.DeviceNameEntry = Entry(self)
        self.DeviceNameEntry.grid(row = 0, column = 4, sticky = W)
        
        self.instruction2 = Label(self, text = "Tyveri ID: ")
        self.instruction2.grid(row = 0, column = 5, columnspan = 1, sticky = W)
        
        self.DeviceTyvEntry = Entry(self)
        self.DeviceTyvEntry.grid(row = 0, column = 6, sticky = W)
        
        self.text = Text(self, width = 60, height = 30, wrap = WORD)
        self.text.grid(row = 1, column = 2, columnspan = 10, sticky = W)
        
        self.AddComButton = Button(self, text = "Tilfoj ny device", command = self.somthing)
        self.AddComButton.grid(row = 2, column = 2, sticky = W)
        
    def somthing(self):
        dType = self.DeviceTypeEntry.get()
        name = self.DeviceNameEntry.get()
        tyv = self.DeviceTyvEntry.get()
        if (len(dType) >= 1) and (len(name) >= 1) and (len(tyv) >= 1):
            checker = c.execute("Select * From Device Where type = ? AND navn = ? AND tyverid = ?", (dType, name, tyv)).fetchall()
            if len(checker) == 0:
                c.execute("INSERT INTO Device(type, navn, tyverid) VALUES (?, ?, ?)", (dType, name, tyv))
                db.commit()
                message = "Ny" + dType + "tilfojet til systemet"
            else:
                message = "En device er allerede i systemet"
            self.text.delete(0.0, END)
            self.text.insert(0.0, message)
                
root = Tk()
root.title("Tilfoj ny computer")
root.geometry("550x550")
app = Application(root)

root.mainloop()