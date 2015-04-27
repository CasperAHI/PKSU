import sqlite3
import datetime



con = sqlite3.connect(r"KEAbib.db")
conn = sqlite3.connect("KEAbib.db")
sqlCon = sqlite3.connect("KEAbib.db").cursor()

'''
sqlCon.execute("""CREATE TABLE Bruger (
                brugerid INTEGER PRIMARY KEY AUTOINCREMENT,
                mail TEXT,
                navn TEXT,
                telefon INT )""")

sqlCon.execute("""CREATE TABLE Computer  (
                computerid INTEGER PRIMARY KEY AUTOINCREMENT,
                navn TEXT,
                tyverid INT )""")

sqlCon.execute("""CREATE TABLE Loan (
                bid INT,
                cid INT,
                loan datetime,
                delivered datetime,
                FOREIGN KEY(bid) REFERENCES Bruger(brugerid),
                FOREIGN KEY(cid) REFERENCES Computer(computerid) )""")'''
try:
    sqlCon.execute("INSERT INTO Bruger(mail, navn, telefon) VALUES ('blahblah@blah.blah' , 'Casper' , '11223344')")
    conn.commit()
except:
    conn.rollback()

print(sqlCon.execute("Select * From loan").fetchall())


