import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Bruger(models.Model):
    bruger_text = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.bruger_text
        
class Device(models.Model):
    device_text = models.CharField(max_length=200)
    device_type = models.CharField(max_length=50)
    device_theft = models.IntegerField
    
    
class Loan(models.Model):
    bruger = models.ForeignKey(Bruger)
    device = models.ForeignKey(Device)
    loan_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published')
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.device_text
        
sqlCon.execute("""CREATE TABLE Device  (
                deviceid INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                navn TEXT,
                tyverid INT )""")

sqlCon.execute("""CREATE TABLE Loan (
                bid INT,
                did INT,
                loan datetime,
                delivered datetime,
                FOREIGN KEY(bid) REFERENCES Bruger(brugerid),
                FOREIGN KEY(did) REFERENCES Device(deviceid) )""")'''