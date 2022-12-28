from django.contrib import admin
from .models import notifications, student,teacher,verifylogin,hod,materials,announcement,loginstatus,subject,work,chatting,sworks,tutors,academicyear,substatus,grading,grade,marks,creditreq,feedback,notifications

# Register your models here.
admin.site.register(student)
admin.site.register(verifylogin)
admin.site.register(teacher)
admin.site.register(hod)
admin.site.register(materials)
admin.site.register(announcement)
admin.site.register(loginstatus)
admin.site.register(subject)
admin.site.register(work)
admin.site.register(chatting)
admin.site.register(sworks)
admin.site.register(academicyear)
admin.site.register(tutors)
admin.site.register(substatus)
admin.site.register(grading)
admin.site.register(grade)
admin.site.register(marks)
admin.site.register(creditreq)
admin.site.register(feedback)
admin.site.register(notifications)