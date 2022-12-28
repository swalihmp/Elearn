from ast import Return
import imp
from logging.config import valid_ident
from msilib import CreateRecord
from multiprocessing import context
from pickle import NONE
from site import venv
from ssl import VerifyFlags
from xmlrpc.client import DateTime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from .models import chatting, creditreq, marks,materials, notifications,student,verifylogin,teacher,hod,announcement,loginstatus,subject,work,sworks,tutors,academicyear,substatus,materials,grading,marks,creditreq,feedback,notifications
from datetime import datetime
from django.db.models import Sum


# Create your views here.

def add_stud(request):
    if request.method == 'POST':
        adnum = request.POST['adnum']
        name = request.POST['name']
        dob = request.POST['dob']
        mob = request.POST['mob']
        sdptname = request.POST['sdptname']
        semno = request.POST['semno']
        year = request.POST['year']
        simage = request.FILES['simage']
        ukey = "s"
        new_stud = student(adnum = adnum,name = name,dob = dob,mob = mob,sdptname = sdptname,semno = semno,year = year,simage = simage)
        new_role = verifylogin(uid = adnum,uname = name,upass = dob,ukey = ukey)
        new_role.save()
        new_stud.save()
        return HttpResponse('Added')
    elif request.method == 'GET':
        return render(request, 'addstud.html')
    else:
        return HttpResponse("Not Added")
    

def stud_profile(request):
    userid = val()
    results = student.objects.filter(adnum = userid)
    return render(request,'stud_profile.html',{"profile":results})
def teach_profile(request):
    userid = val()
    results = teacher.objects.filter(tid = userid)
    return render(request,'teach_profile.html',{"profile":results})


def shome(request):
    userid = val()
    sems = student.objects.get(adnum = userid)
    semno = sems.semno
    results = student.objects.filter(adnum = userid)
    results1 = notifications.objects.filter(semno = semno)
    return render(request,'shome.html',{"showstud":results,"showmsg":results1})


def hodhome(request):
    userid = val()
    results = hod.objects.filter(hid = userid)
    return render(request,'hodhome.html',{"showhod":results})
def teachhome(request):
    userid = val()
    results = teacher.objects.filter(tid = userid)
    return render(request,'teachhome.html',{"showteach":results})

def addtutor(request):
    userid = val()
    hods = hod.objects.get(hid = userid)
    dpt = hods.hdpt
    results = teacher.objects.filter(dptname = dpt)
    results1 = hod.objects.filter(hid = userid)
    results2 = academicyear.objects.all
    return render(request,'addtutor.html',{'teachers':results,'department':results1,'years':results2})

def add_tutor(request):
    if request.method == 'POST':
        userid = val()
        year = request.POST['year']
        dpt = request.POST['hdpt']
        tutor = request.POST['tname']
        new_tutor = tutors(year = year,dpt = dpt,tutor = tutor,createby = userid)
        new_tutor.save()
        return HttpResponse("Added")
    else:
        return HttpResponse("Not Added")


def showstud(request):
    userid = val()
    results = hod.objects.filter(hid = userid)
    return render(request,'showstud.html',{"showdpt":results})
def studli(request):
    if request.method == 'POST':
        userid = val()
        dptname = request.POST['dptname']
        semno = request.POST['semno']
        results = hod.objects.filter(hid = userid)
        students = student.objects.filter(sdptname = dptname,semno = semno)
        return render(request,'showstud.html',{'students':students,'showdpt':results})
        

def ancmnts(request):
    userid = val()
    results = hod.objects.filter(hid = userid)
    return render(request,'announcmnt.html',{"showdpt":results})
def add_ancm(request):
    if request.method == 'POST':
        dptname = request.POST['dptname']
        anmsg = request.POST['anmsg']
        new_ancmnt = announcement(anmsg = anmsg,dptname = dptname)
        new_ancmnt.save()
        return HttpResponse('Added')
        

def adminhome(request):
    return render(request,'adminhome.html')
def login_view(request):
    return render(request,'login.html')
def addteach(request):
    return render(request,'addteach.html')
def addhod(request):
    return render(request,'addhod.html')
def smenu(request):
    return render(request, 'smenu.html')
def liveclass(request):
    return render(request, 'liveclass/index.html')

def add_mater(request):
    userid = val()
    results = subject.objects.filter(subteachid = userid)
    return render(request,'addmaterial.html',{"showsub":results})
def addmater(request):
    if request.method == 'POST':
        subname = request.POST['subname']
        mater = request.FILES['mater']
        new_mater = materials(subname = subname,material = mater)
        new_mater.save()
        return HttpResponse('Uploaded')
        
        
def addwork(request):
    userid = val()
    results = teacher.objects.filter(tid = userid)
    results1 = subject.objects.filter(subteachid = userid)
    return render(request,'addwork.html',{"showdpt":results,"showdpt1":results1})
def add_work(request):
    if request.method == 'POST':
        workname = request.POST['workname']
        dptname = request.POST['dptname']
        semno = request.POST['semno']
        subname = request.POST['subname']
        defwork = request.POST['defwork']
        wfile = request.FILES['wfile']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        msg = "New Work Has Been Added"
        new_work = work(workname = workname,dptname = dptname,semno = semno,subname = subname,defwork = defwork,wfile = wfile,sdate = sdate,edate = edate)
        new_msg = notifications(msg = msg,dptname = dptname,semno = semno,subname = subname)
        new_msg.save()
        new_work.save()
        return HttpResponse('Added')
    elif request.method == 'GET':
        return HttpResponse("Not Added")
    else:
        return HttpResponse("Not Added")

def uploadwork(request,workid):
    if request.method == 'POST':
        userid = val()
        sfile = request.FILES['sfile']
        sdate = datetime.now()
        works = work.objects.get(workid = workid)
        wsname = works.subname
        wname = works.workname
        studname = student.objects.get(adnum = userid)
        sname = studname.sname
        new_file = sworks(workid = workid,wname = wname,wsname = wsname,sid = userid,sname = sname,udate = sdate,sfile = sfile)
        new_file.save()
        return HttpResponse("Submitted")
    else:
        return render(request,'course.html')

        
def addstud(request):
    userid = val()
    results = teacher.objects.filter(tid = userid)
    results1 = academicyear.objects.all()
    return render(request,'addstud.html',{"showdpt":results,"showyear":results1})
        

    
def add_teach(request):
    if request.method == 'POST':
        tid = request.POST['tid']
        tname = request.POST['tname']
        tdob = request.POST['tdob']
        tmob = request.POST['tmob']
        dptname = request.POST['dptname']
        timage = request.FILES['timage']
        ukey = "t"
        
        new_teach = teacher(tid = tid,tname = tname,tdob = tdob,tmob = tmob,dptname = dptname,timage = timage)
        new_role = verifylogin(uid = tid,uname = tname,upass = tdob,ukey = ukey)
        new_role.save()
        new_teach.save()
        return HttpResponse('Teacher Added')
    elif request.method == 'GET':
        return render(request, 'addteach.html')
    else:
        return HttpResponse("Not Added")
    
def add_hod(request):
    if request.method == 'POST':
        hid = request.POST['hid']
        hname = request.POST['hname']
        hdob = request.POST['hdob']
        hmob = request.POST['hmob']
        hdpt = request.POST['hdpt']
        himage = request.FILES['himage']
        ukey = "h"
        
        new_hod = hod(hid = hid,hname = hname,hdob = hdob,hmob = hmob,hdpt = hdpt,himage = himage)
        new_role = verifylogin(uid = hid,uname = hname,upass = hdob,ukey = ukey)
        new_role.save()
        new_hod.save()
        return HttpResponse('Hod Added')
    elif request.method == 'GET':
        return render(request, 'addhod.html')
    else:
        return HttpResponse("Not Added")
val = None
  
def loginview(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        upass = request.POST['upass']
        global val
        def val():
            return uid
        if verifylogin.objects.filter(uid = uid,upass = upass,ukey = "s").exists():
            toflogin = datetime.now()
            new_loginstat = loginstatus(uid = uid,toflogin = toflogin)
            new_loginstat.save()
            return redirect('shome')
        elif verifylogin.objects.filter(uid = uid,upass = upass,ukey = "t").exists():
            toflogin = datetime.now()
            new_loginstat = loginstatus(uid = uid,toflogin = toflogin)
            new_loginstat.save()
            return redirect('teachhome')
        elif verifylogin.objects.filter(uid = uid,upass = upass,ukey = "h").exists():
            toflogin = datetime.now()
            new_loginstat = loginstatus(uid = uid,toflogin = toflogin)
            new_loginstat.save()
            return redirect('hodhome')
        else :
            return HttpResponse("Invalid Credentials")
    else :
        return HttpResponse("Error")
    
def changpass(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        opass = request.POST['opass']
        npass = request.POST['npass']
        if verifylogin.objects.filter(uid = uid,upass = opass).exists():
            credentials = verifylogin.objects.get(uid = uid)
            credentials.uid=uid
            credentials.upass=npass
            credentials.save()
            messages.add_message(request,messages.ERROR,"Password Updates Successfully")
            return render(request, 'changpass.html')
        else:
            messages.add_message(request,messages.ERROR,"Invalid Old Credentials")
            return render(request, 'changpass.html')
    else:
        return render(request, 'changpass.html')
    
def update_stud(request):
    if request.method == 'POST':
        nuid = request.POST['adnum']
        nname = request.POST['name']
        ndob = request.POST['dob']
        nmob = request.POST['mob']
        nsdptname = request.POST['sdptname']
        nsemno = request.POST['semno']
        if student.objects.filter(adnum = nuid).exists():
            credentials = student.objects.get(adnum = nuid)
            credentials.adnum=nuid
            credentials.name=nname
            credentials.dob=ndob
            credentials.mob=nmob
            credentials.sdptname=nsdptname
            credentials.semno=nsemno
            credentials.save()
            messages.add_message(request,messages.ERROR,"Student Updated Successfully")
            return render(request, 'showstud.html')
        else:
            messages.add_message(request,messages.ERROR,"Admission Number Wont be changed")
            return render(request, 'editstud.html')
    else:
        return render(request, 'editstud.html')
        
        
    
def add_sub(request):
    userid = val()
    results = teacher.objects.filter(tid = userid)
    return render(request,'addsub.html',{"showdpt":results})  
def addsub(request):
    if request.method == 'POST':
        subdpt = request.POST['subdpt']
        subcode = request.POST['subcode']
        subname = request.POST['subname']
        subcredit = request.POST['subcredit']
        subsemno = request.POST['subsemno']
        subteach = request.POST['subteach']
        subteachid = request.POST['subteachid']
        
        new_sub = subject(subdpt=subdpt , subcode = subcode, subname = subname, subcredit = subcredit, subsemno = subsemno, subteach = subteach, subteachid = subteachid)
        new_sub.save()
        return HttpResponse('Subject Added')
    elif request.method == 'GET':
        return render(request, 'addsub.html')
    else:
        return HttpResponse("Not Added")

def viewcourse(request):
    userid = val()
    studsem = student.objects.get(adnum = userid)
    semno = studsem.semno
    sdptname = studsem.sdptname
    results = subject.objects.filter(subsemno = semno,subdpt = sdptname)
    return render(request,'viewcourse.html',{"showsub":results})
val1 = None
def course(request,subname):
    userid = val()
    global val1
    def val1():
        return subname
    if request.method == 'POST':
        sdate = datetime.now()
        enddate = work.objects.get(subname = subname)
        edate = enddate.edate
        subworks= work.objects.filter(subname = subname, edate__range = [sdate , edate])
        
        studs = chatting.objects.filter(stud_id = userid,subname = subname)
        results = subject.objects.filter(subname = subname)
        status = substatus.objects.filter(subname = subname)
        return render(request,'course.html',{"showcourse":results,"studmsg":studs,"subworks":subworks,"substatus":status})
    else:
        return render(request,'course.html')
    
def chattstud(request,subteachid):
    if request.method == 'POST':
        subname = val1()
        userid = val()
        teachid = subteachid
        stud_name = student.objects.get(adnum = userid)
        stud_name = stud_name.name
        quest = request.POST['quest']
        newmsg = chatting(subname = subname,stud_id = userid,stud_name = stud_name,teach_id = teachid,quest = quest)
        newmsg.save()
        return HttpResponse('Question Added')
def showchat(request):
    userid = val()
    chats = chatting.objects.filter(teach_id = userid)
    return render(request,'chatt.html',{"chatting":chats})
def chatreplay(request,chatid):
    if request.method == 'POST':
        replay = request.POST['replay']
        if chatting.objects.filter(chatid = chatid).exists():
           credentials = chatting.objects.get(chatid = chatid)
           credentials.replay=replay
           credentials.save()
           messages.add_message(request,messages.ERROR,"Replied")
           return render(request,'chatt.html')
    else:
        return render(request, 'chatt.html')   
        
def gradings(request):
    userid = val()
    studsem = student.objects.get(adnum = userid)
    semno = studsem.semno
    sdptname = studsem.sdptname
    results1 = subject.objects.filter(subsemno = semno,subdpt = sdptname)
    return render(request,'grading.html',{"showsubs":results1})
val2 = None
def workes(request):
    if request.method == 'POST':
        userid = val()
        studsem = student.objects.get(adnum = userid)
        semno = studsem.semno
        sdptname = studsem.sdptname
        results1 = subject.objects.filter(subsemno = semno,subdpt = sdptname)
        subname = request.POST['subname']
        global val2
        def val2():
            return subname
        works = sworks.objects.filter(wsname = subname)
        return render(request, 'grading.html',{"showworks":works,"showsubs":results1})
val3 = None
def show_file(request):
    if request.method == 'POST':
        userid = val()
        studsem = student.objects.get(adnum = userid)
        semno = studsem.semno
        sdptname = studsem.sdptname
        results1 = subject.objects.filter(subsemno = semno,subdpt = sdptname)
        subname = val2()
        works = sworks.objects.filter(wsname = subname)
        sname = request.POST['sname']
        global val3
        def val3():
            return sname
        file = sworks.objects.filter(wsname = subname,sname = sname)
        return render(request, 'grading.html',{"showfiles":file,"showworks":works,"showsubs":results1})
def add_grade(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        feedback = request.POST['feedback']
        userid = val()
        wsname = val2() 
        sname = val3()   
        sids = sworks.objects.get(wsname = wsname,sname = sname)
        sid = sids.sid 
        wname = sids.wname
        tofgrd = datetime.now()
        new_grade = grading(uid = userid,sid = sid,wname = wname,rating = rating,tofgrd = tofgrd,feedback = feedback)
        new_grade.save()
        return HttpResponse('Graded')
        
    

def sgpa(request):
    userid = val()
    results = student.objects.filter(adnum = userid)
    return render(request,'sgpa.html',{"showdpt":results})
def view_credit(request):
    if request.method == 'POST':
        userid = val()
        results = student.objects.filter(adnum = userid)
        dptname = request.POST['dptname']
        semno = request.POST['semno']
        credits = subject.objects.filter(subdpt = dptname,subsemno = semno)
        return render(request, 'sgpa.html',{"viewcredit":credits,"showdpt":results})

def sub_map(request):
    userid = val()
    subjects = subject.objects.filter(subteachid = userid)
    return render(request,'submap.html',{"showsub":subjects})

def submap(request):
    if request.method == 'POST':
        userid = val()
        subname = request.POST['subname']
        status = request.POST['status']
        stime = datetime.now()
        new_status = substatus(userid = userid, subname = subname, status = status, stime = stime)
        new_status.save()
        return HttpResponse('Status Added')

def addmark(request):
    userid = val()
    results1 = subject.objects.filter(subteachid = userid)
    return render(request,'addmark.html',{"showdpt1":results1})

val4 = None
def view_works(request):
    if request.method == 'POST':
        userid = val()
        results1 = subject.objects.filter(subteachid = userid)
        subname = request.POST['subname']
        global val4
        def val4():
            return subname
        works = work.objects.filter(subname = subname)
        return render(request,'addmark.html',{"workes":works,"showdpt1":results1})
val5 = None
def show_works(request):
    if request.method == 'POST':
        userid = val()
        results1 = subject.objects.filter(subteachid = userid)
        
        workname = request.POST['workname']
        global val5
        def val5():
            return workname
        subname = val4()
        
        works = work.objects.filter(subname = subname)
        studs = sworks.objects.filter(wname = workname,wsname = subname)
        return render(request,'addmark.html',{"students":studs,"workes":works,"showdpt1":results1})
val6 = None
def show_files(request):
    if request.method == 'POST':
        userid = val()
        results1 = subject.objects.filter(subteachid = userid)
        sname = request.POST['studname']
        global val6
        def val6():
            return sname
        subname = val4()
        wname = val5()
        works = work.objects.filter(subname = subname)
        studs = sworks.objects.filter(wname = wname,wsname = subname)
        sfiles = sworks.objects.filter(sname = sname,wsname = subname,wname = wname)
        return render(request,'addmark.html',{"files":sfiles,"students":studs,"workes":works,"showdpt1":results1})
def add_mark(request):
    if request.method == 'POST':
        mark = request.POST['mark']
        wsname = val4()
        wname = val5()
        sname = val6()
        sids = student.objects.get(name = sname)
        sid = sids.adnum
        new_mark = marks(uid = sid,subname = wsname,wname = wname,mark = mark)
        new_mark.save()
        return HttpResponse('Mark Added')
    
def viewcredit(request):
    credits = creditreq.objects.all()
    return render(request, 'credits.html',{"credit":credits})

def showmarks(request):
    userid = val()
    datas = marks.objects.filter(uid = userid)
    return render(request, 'showmarks.html',{"viewmark":datas})

def add_feedback(request):
    return render(request,'feedback.html')    
def addfeedback(request):
    if request.method == 'POST':
        userid = val()
        ftime = datetime.now()
        msg = request.POST['feedback']
        new_msg = feedback(uid = userid,feedback = msg,toffb = ftime)
        new_msg.save()
        return HttpResponse('Feedback Saved')
    
def editstud(request,adnum):
    if request.method == 'POST':
        userid = val()
        stud = student.objects.filter(adnum = adnum)
        result = hod.objects.filter(hid = userid)
        return render(request, 'editstud.html',{"viewstud":stud,"showdpt":result})