# -*- coding: utf-8 -*-

import sqlite3

db = sqlite3.connect('KEAbib.db')
c = db.cursor()
def ledige():
    l = c.execute('SELECT * FROM Device WHERE deviceid = (SELECT did FROM Loan WHERE delivered != null)').fetchall()
    return l

def udlaant():
    u = c.execute('SELECT * FROM Device WHERE deviceid = (SELECT did FROM Loan WHERE delivered = null)').fetchall()
    return u
    
def udlaan(computerNavn, brugerNavn):
    c.execute('INSERT INTO Loan VALUES (SELECT brugerid FROM Bruger WHERE navn = brugerNavn, SELECT deviceid FROM Device WHERE navn = deviceNavn,now())')

def aflever(computerNavn):
    c.execute('UPDATE Loan SET delivered = timestamp WHERE did = (SELECT deviceid FROM Device WHERE navn = computerNavn)')
    
def brugerHistorik(brugerNavn):
    h = c.execute('SELECT * FROM Bruger WHERE navn = brugerNavn').fetchall
    return h

def computerHistorik(deviceNavn):
    h = c.execute('SELECT * FROM Device WHERE navn = deviceNavn').fetchall
    return h

print(3)
print (ledige())