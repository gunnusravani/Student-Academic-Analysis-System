
from configparser import SafeConfigParser
from http.server import ThreadingHTTPServer
from django.shortcuts import render,redirect # allows us to redirect user to another page
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Sum,Count,Value
from django.shortcuts import render
from .models import Mid_1_1, Results_1_1,Results_1_2
from .models import Results_2_1,Results_2_2
from .models import Results_3_1,Results_3_2
from .models import Results_4_1,Results_4_2

from .models import Student,Results_1_1
from .models import Mid_1_1,Mid_1_2,Mid_2_1,Mid_2_2,Mid_3_1,Mid_3_2,Mid_4_1,Mid_4_2
# Create yo
# ur views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect ('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'User name Already used')
                return redirect ('register')
            else :
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password is not same')
            return redirect ('register')
    else:
        return render(request,'register.html')

def login(request):
    global x
    if request.method =='POST':
        username = request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(request,user)
            return redirect('results')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def update(request):
    
    SGPA=[]
    CG=[]
    credits=[]
    if request.method =='POST':
            students=Student.objects.all()
            for i in students:
                if Results_1_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_1_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_1_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S1=round(s/k['C'],2)
                    i.SGPA_1_1 = S1
                    i.save()
                    SGPA.append(S1)
                    credits.append(k['C'])

                if Results_1_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_1_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_1_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S2=round(s/k['C'],2)
                    i.SGPA_1_2 = S2
                    i.save()
                    SGPA.append(S2)
                    credits.append(k['C'])

                if Results_2_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_2_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_2_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S3=round(s/k['C'],2)
                    i.SGPA_2_1 = S3
                    i.save()
                    SGPA.append(S3)
                    credits.append(k['C'])

                if Results_2_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_2_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_2_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S4=round(s/k['C'],2)
                    i.SGPA_2_2 = S4
                    i.save()
                    SGPA.append(S4)
                    credits.append(k['C'])

                if Results_3_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_3_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_3_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S5=round(s/k['C'],2)
                    i.SGPA_3_1 = S5
                    i.save()
                    SGPA.append(S5)
                    credits.append(k['C'])

                if Results_3_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_3_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_3_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S6=round(s/k['C'],2)
                    i.SGPA_3_2 = S6
                    i.save()
                    SGPA.append(S6)
                    credits.append(k['C'])

                if Results_4_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_4_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_3_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S7=round(s/k['C'],2)
                    i.SGPA_4_1 = S7
                    i.save()
                    SGPA.append(S7)
                    credits.append(k['C'])

                if Results_4_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_4_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_4_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S8=round(s/k['C'],2)
                    i.SGPA_4_2 = S8
                    i.save()
                    SGPA.append(S8)
                    credits.append(k['C'])
                messages.info(request, 'Updated Successfully')

                CG = [SGPA[i]*credits[i] for i in range(len(SGPA))]
                if (sum(credits)!=0):
                     i.CGPA = round(sum(CG)/sum(credits),2)
                     i.save()
                

    return render(request, 'update.html') 

def results(request):
    # Sem marks
    context1={}
    context2={}
    context3={}
    context4={}
    CGPA=[]
    SGPA1={}
    students=[]
    midmarks1={}
    midmarks2={}
    midmarks3={}
    midmarks4={}
    
    
    
    if request.method =='POST':
        roll= request.POST['roll']
        if Student.objects.filter(roll_no=roll).exists():
            student=Student.objects.filter(roll_no=roll)
            students.append(student)
            if Results_1_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_1_1.objects.filter(Htno=roll)
                    context1['1_1']=data1
                    for i in student:
                       SGPA1['1_1']=i.SGPA_1_1
            
            #2ND
  
            if Results_1_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_1_2.objects.filter(Htno=roll)
                    context1['1_2']=data1
                    for i in student:
                       SGPA1['1_2']=i.SGPA_1_2
            
            # 3RD
            if Results_2_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_2_1.objects.filter(Htno=roll)
                    context2['2_1']=data1
                    for i in student:
                       SGPA1['2_1']=i.SGPA_2_1

            if Results_2_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_2_2.objects.filter(Htno=roll)
                    context2['2_2']=data1
                    for i in student:
                       SGPA1['2_2']=i.SGPA_2_2
            
            if Results_3_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_3_1.objects.filter(Htno=roll)
                    context3['3_1']=data1
                    for i in student:
                       SGPA1['3_1']=i.SGPA_3_1

            if Results_3_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_3_2.objects.filter(Htno=roll)
                    context3['3_2']=data1
                    for i in student:
                       SGPA1['3_2']=i.SGPA_3_2

            if Results_4_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_4_1.objects.filter(Htno=roll)
                    context4['4_1']=data1
                    for i in student:
                       SGPA1['4_1']=i.SGPA_4_1

            if Results_4_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_4_2.objects.filter(Htno=roll)
                    context4['4_2']=data1
                    for i in student:
                       SGPA1['4_2']=i.SGPA_4_2
            
            CGPA.append(Student.CGPA)
        
            #sem_name={'sem':{'data1':S1,'data2':S2,'data3':S3,'data4':S4,'data5':S5,'data6':S6,'data7':S7,'data8':S8}}
            if  Mid_1_1.objects.filter(HTNO = roll).exists() :
                m1= Mid_1_1.objects.filter(HTNO = roll)
                midmarks1['1_1']=m1
            
            if  Mid_1_2.objects.filter(HTNO = roll).exists() :
                m2= Mid_1_2.objects.filter(HTNO = roll)
                midmarks1['1_2']=m2
            
            if  Mid_2_1.objects.filter(HTNO = roll).exists() :
                m3= Mid_2_1.objects.filter(HTNO = roll)
                midmarks2['2_1']=m3

            if  Mid_2_2.objects.filter(HTNO = roll).exists() :
                m4= Mid_2_2.objects.filter(HTNO = roll)
                midmarks2['2_2']=m4

            if  Mid_3_1.objects.filter(HTNO = roll).exists() :
                m5= Mid_3_1.objects.filter(HTNO = roll)
                midmarks3['3_1']=m5

            if  Mid_3_2.objects.filter(HTNO = roll).exists() :
                m6= Mid_3_2.objects.filter(HTNO = roll)
                midmarks3['3_2']=m6
            
            if  Mid_4_1.objects.filter(HTNO = roll).exists() :
                m7= Mid_4_1.objects.filter(HTNO = roll)
                midmarks4['4_1']=m7

            if  Mid_4_2.objects.filter(HTNO = roll).exists() :
                m8= Mid_4_2.objects.filter(HTNO = roll)
                midmarks4['4_2']=m8
            
    
    return render(request,"results.html",{'data1':context1,'data2':context2,'data3':context3,'data4':context4,'SGPA':SGPA1,'CGPA':CGPA,'student':students,'mid1':midmarks1,'mid2':midmarks2,'mid3':midmarks3,'mid4':midmarks4})



    

