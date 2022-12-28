from asyncio.constants import _SendfileMode
from copyreg import add_extension
from datetime import timedelta
from email.policy import default
from plistlib import UID
from threading import get_ident
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
# Create your models here.

class teacher(models.Model):
    tid = models.CharField(max_length=10, default=0) 
    tname = models.CharField(max_length=100, null=False) 
    tdob = models.DateField()
    tmob = models.IntegerField(default=0)
    dptname = models.CharField(max_length=100, null=False)
    timage = models.FileField(default=0)
    
class hod(models.Model):
    hid = models.CharField(max_length=10, default=0) 
    hname = models.CharField(max_length=100, null=False) 
    hdob = models.DateField()
    hmob = models.IntegerField(default=0)
    hdpt = models.CharField(max_length=100, null=False)
    himage = models.FileField(default=0)
    
class student(models.Model):
    adnum = models.CharField(max_length=10, default=0) 
    name = models.CharField(max_length=100, null=False)
    dob = models.DateField()
    mob = models.IntegerField(default=0)
    sdptname = models.CharField(max_length=50, default=0, null=False)
    semno = models.CharField(max_length=10, default=0, null=False)
    year = models.CharField(max_length=20, default=0)
    simage = models.FileField(default=0)
    
class verifylogin(models.Model):
    uid = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    upass = models.CharField(max_length=50)
    ukey = models.CharField(max_length=50)
    
class loginstatus(models.Model):
    uid = models.CharField(max_length=10)
    toflogin = models.DateTimeField()      


    
class announcement(models.Model): 
    anmsg = models.CharField(max_length=50)
    dptname = models.CharField(max_length=15)    
    

    
class subject(models.Model):
    subdpt = models.CharField(max_length=10)
    subcode = models.CharField(max_length=10)
    subname = models.CharField(max_length=10)
    subcredit = models.CharField(max_length=10,default=4)
    subsemno = models.IntegerField(max_length=10)
    subteach = models.CharField(max_length=10) 
    subteachid = models.CharField(max_length=10)
    
class materials(models.Model):
    subname = models.CharField(max_length=20)
    material = models.FileField(default=0)
    
class grade(models.Model):
    gid = models.CharField(max_length=20,default=0)
    gpoint = models.CharField(max_length=20,default=0)


class work(models.Model):
    workid = models.AutoField(primary_key=True)
    workname = models.CharField(max_length=50,default=0)
    dptname = models.CharField(max_length=45)
    semno = models.CharField(max_length=10)
    subname = models.CharField(max_length=45)
    defwork = models.CharField(max_length=45, blank=True, null=True)
    wfile = models.FileField(default=0)
    sdate = models.DateField(blank=True, null=True)
    edate = models.DateTimeField(blank=True, null=True)
    
class sworks(models.Model):
    workid = models.CharField(max_length=3)
    wname = models.CharField(max_length=50,default=0)
    wsname = models.CharField(max_length=20,default=0)
    sid = models.CharField(max_length=5)
    sname = models.CharField(max_length=20,default=0)
    udate = models.DateTimeField(blank=True, null=True)
    sfile = models.FileField(default=0) 
    
    

class chatting(models.Model):
    chatid = models.AutoField(primary_key=True)
    subname = models.CharField(max_length=10)
    stud_id = models.CharField(max_length=10)
    stud_name = models.CharField(max_length=10)
    teach_id = models.CharField(max_length=10)
    status = models.CharField(max_length=10,default=000)
    quest = models.CharField(max_length=50)
    replay = models.CharField(max_length=50)

class tutors(models.Model):
    year = models.CharField(max_length=10)
    dpt = models.CharField(max_length=10)
    tutor = models.CharField(max_length=10)
    createby = models.CharField(max_length=10)
    
class academicyear(models.Model):
    year = models.CharField(max_length=10)
    
class substatus(models.Model):
    userid = models.CharField(max_length=10)
    subname = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    stime = models.DateTimeField(blank=True, null=True)
    
class grading(models.Model):
    uid = models.CharField(max_length=10)
    sid = models.CharField(max_length=10)
    wname = models.CharField(max_length=10)
    rating = models.CharField(max_length=10)
    tofgrd = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=10)
    
class marks(models.Model):
    uid = models.CharField(max_length=50)
    subname = models.CharField(max_length=50)
    wname = models.CharField(max_length=50)
    mark = models.FloatField()
    total = models.FloatField(null=True)
    
class creditreq(models.Model):
    semno = models.CharField(max_length=50)
    creditallo = models.CharField(max_length=50)
    creditmin = models.CharField(max_length=50)
    
class feedback(models.Model):
    uid = models.CharField(max_length=50)
    feedback = models.CharField(max_length=50)
    toffb = models.DateTimeField(null=True)

class notifications(models.Model):
    msg = models.CharField(max_length=50)
    subname = models.CharField(max_length=50,default=0)
    dptname = models.CharField(max_length=20)
    semno = models.CharField(max_length=10)
    