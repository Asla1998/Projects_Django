from django.shortcuts import render,redirect
from .models import donor,receiver,blood_req,blog
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate



# common

def index(request):
    return render(request,'common/index.html')

def login(request):
    return render(request,'common/login.html')

def about(request):
    return render(request,'common/about.html')    

def blogs(request):
    return render(request,'common/blog.html') 

def contact(request):
    return render(request,'common/contact.html')  
   
def donors(request):
    return render(request,'common/donor.html')            

# admin

def admindashboard(request):
    return render(request,'admin/admindashboard.html') 

def adminblogadd(request):
    return render(request,'admin/adminaddblog.html')     

def adminpenddonor(request):
    donorlist=donor.objects.all()
    return render(request,'admin/adminpenddonor.html',{'donorlist':donorlist}) 
    
def admindonor(request):
    donorlist=donor.objects.all()
    return render(request,'admin/admindonor.html',{'donorlist':donorlist})   

def adminapprovedonor(request,donor_id):
    donorlist=donor.objects.get(id=donor_id)
    donorlist.status=1
    donorlist.save()
    return redirect('admindonor') 

def adminrejectdonor(request,donor_id):
    donorlist=donor.objects.get(id=donor_id)
    donorlist.delete()
    return redirect('adminpenddonor')  

def admindeletedonor(request,donor_id):
    donorlist=donor.objects.get(id=donor_id)
    donorlist.delete()
    return redirect('admindonor') 

def adminpendreceiver(request):
    receiverlist=receiver.objects.all()
    return render(request,'admin/adminpendreceiver.html',{'receiverlist':receiverlist}) 
    
def adminreceiver(request):
    receiverlist=receiver.objects.all()
    return render(request,'admin/adminreceiver.html',{'receiverlist':receiverlist})   

def adminapprovereceiver(request,receiver_id):
    receiverlist=receiver.objects.get(id=receiver_id)
    receiverlist.status=1
    receiverlist.save()
    return redirect('adminreceiver') 

def adminrejectreceiver(request,receiver_id):
    receiverlist=receiver.objects.get(id=receiver_id)
    receiverlist.delete()
    return redirect('adminpendreceiver')  

def admindeletereceiver(request,receiver_id):
    receiverlist=receiver.objects.get(id=receiver_id)
    receiverlist.delete()
    return redirect('adminreceiver') 

def adminpendreqblood(request):
    donorlist = donor.objects.all().prefetch_related('donordetail')
    return render(request,'admin/adminpendreqblood.html',{'donorlist':donorlist})

def adminreqblood(request):
    donorlist = donor.objects.all().prefetch_related('donordetail')
    return render(request,'admin/adminapprovereq.html',{'donorlist':donorlist})    

def adminapprovereqblood(request,req_id):
    reqlist=blood_req.objects.get(id=req_id)
    reqlist.status=1
    reqlist.save()
    return redirect('adminreqblood') 

def adminrejectreqblood(request,req_id):
    reqlist=blood_req.objects.get(id=req_id)
    reqlist.delete()
    return redirect('adminpendreqblood')   

def admindeletereqblood(request,req_id):
    reqlist=blood_req.objects.get(id=req_id)
    reqlist.delete()
    return redirect('adminreqblood')      

def adminaddblog(request):
    bloglist=blog.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        blog_img=request.FILES['blog_img']
        description=request.POST.get('description')
        bloger_img=request.FILES['bloger_img']
        name=request.POST.get('name')
        date=request.POST.get('date')
        bloglist1=blog(title=title,blog_img=blog_img,description=description,bloger_img=bloger_img,name=name,date=date)
        bloglist1.save()
        return redirect('adminblog')

def adminblog(request):
    bloglist=blog.objects.all()
    return render(request,'admin/adminblog.html',{'bloglist':bloglist})       

# donor

def donordashboard(request):
    return render(request,'donor/donordashboard.html') 

def donorreg(request):
    return render(request,'donor/donorreg.html')     

def donorregistration(request):
    donorlist=donor.objects.all()
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        donor_img=request.FILES['donor_img']
        blood=request.POST.get('blood')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        job=request.POST.get('job')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        post=request.POST.get('post')
        district=request.POST.get('district')
        country=request.POST.get('country')
        pin=request.POST.get('pin')
        weight=request.POST.get('weight')
        bp=request.POST.get('bp')
        prevdonation=request.POST.get('prevdonation')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        username=request.POST.get('username')
        status='0'
        role='donor'
        
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('donorreg')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Aready Exists")
                return redirect('donorreg')

            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()


                donorlist1=donor(user=user,fullname=fullname,donor_img=donor_img,blood=blood,dob=dob,gender=gender,job=job,phone=phone,email=email,address1=address1,address2=address2,post=post,district=district,country=country,pin=pin,weight=weight,bp=bp,prevdonation=prevdonation,status=status,role=role)
                donorlist1.save()


                print("Donor Created")
        else:
            messages.info(request,"Password is not matching")
            return redirect('donorreg')


        return redirect('index') 
    else:
        return render(request,'donorreg.html') 
    

def donorpendreqblood(request):
    receiverlist = receiver.objects.all().prefetch_related('receiverdetail')
    return render(request,'donor/donorpendreqblood.html',{'receiverlist':receiverlist})

def donorreqblood(request):
    receiverlist = receiver.objects.all().prefetch_related('receiverdetail')
    return render(request,'donor/donorreqblood.html',{'receiverlist':receiverlist})  

def donorapprovereqblood(request,req_id):
    reqlist=blood_req.objects.get(id=req_id)
    reqlist.status=2
    reqlist.save()
    return redirect('donorreqblood') 

def donorrejectreqblood(request,req_id):
    reqlist=blood_req.objects.get(id=req_id)
    reqlist.delete()
    return redirect('donorpendreqblood')   

def donordeletereqblood(request,req_id):
    reqlist=blood_req.objects.get(id=req_id)
    reqlist.delete()
    return redirect('donorreqblood')    

def donorprofile(request):
    if request.user:
        user=request.user
        donorlist=donor.objects.get(user=user)
        return render(request,'donor/donorprofile.html',{'donorlist':donorlist})

def donorprofileupdate(request,donor_id):
    if request.method=="POST":
        donorlist1=donor.objects.get(id=donor_id)
        donorlist1.fullname=request.POST['fullname']
        donorlist1.blood=request.POST['blood']
        donorlist1.gender=request.POST['gender']
        donorlist1.job=request.POST['job']
        donorlist1.phone=request.POST['phone']
        donorlist1.email=request.POST['email']
        donorlist1.address1=request.POST['address1']
        donorlist1.address2=request.POST['address2']
        donorlist1.post=request.POST['post']
        donorlist1.district=request.POST['district']
        donorlist1.country=request.POST['country']
        donorlist1.pin=request.POST['pin']
        donorlist1.weight=request.POST['weight']
        donorlist1.bp=request.POST['bp']
        donorlist1.prevdonation=request.POST['prevdonation']
        donorlist1.save()
        return redirect("donorprofile")
 



    

# receiver

def receiverdashboard(request):
    return render(request,'receiver/receiverdashboard.html')   

def receiverreg(request):
    return render(request,'receiver/receiverreg.html')      


def receiverregistration(request):
    receiverlist=receiver.objects.all()
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        receiver_img=request.FILES['receiver_img']
        blood=request.POST.get('blood')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        job=request.POST.get('job')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        post=request.POST.get('post')
        district=request.POST.get('district')
        country=request.POST.get('country')
        pin=request.POST.get('pin')
        weight=request.POST.get('weight')
        bp=request.POST.get('bp')
        prevreceive=request.POST.get('prevreceive')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        username=request.POST.get('username')
        status='0'
        role='receiver'
        
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('receiverreg')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Aready Exists")
                return redirect('receiverreg')

            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()


                receiverlist1=receiver(user=user,fullname=fullname,receiver_img=receiver_img,blood=blood,dob=dob,gender=gender,job=job,phone=phone,email=email,address1=address1,address2=address2,post=post,district=district,country=country,pin=pin,weight=weight,bp=bp,prevreceive=prevreceive,status=status,role=role)
                receiverlist1.save()


                print("Recipient Created")
        else:
            messages.info(request,"Password is not matching")
            return redirect('receiverreg')


        return redirect('index') 
    else:
        return render(request,'receiverreg.html')              


def receiverdonor(request):
    donorlist=donor.objects.all()
    return render(request,'receiver/receiverdonor.html',{'donorlist':donorlist}) 

def receiverdonordetails(request,donorid):
    donorlist=donor.objects.filter(id=donorid).values()
    print(donorlist)
    return render(request,'receiver/receiverdonordetails.html',{'donorlist':donorlist}) 

def receiverreqblood(request,donors_id):
    if request.user:
        user=request.user 
        donorlist=donor.objects.get(id=donors_id)
        receiverlist=receiver.objects.get(user=user)
        status="0"
        reqlist=blood_req(user=user,donor_id=donorlist,rec_id=receiverlist,status=status)  
        reqlist.save()   
        return redirect('receiverpendreqblood')
        


def receiverpendreqblood(request):
    if request.user:
        user=request.user
        donorlist = donor.objects.all().prefetch_related('donordetail')

        
        return render(request,'receiver/receiverdonorreq.html',{'donorlist':donorlist})

       


def receiverapprovereqblood(request):
    donorlist = donor.objects.all().prefetch_related('donordetail') 
    return render(request,'receiver/receiverapprovereq.html',{'donorlist':donorlist})      

def search(request):
    query=request.GET['query1']
    donorlist=donor.objects.filter(blood__icontains=query)
    return render(request,'receiver/receiverdonorlist.html',{'donorlist':donorlist})    

def receiverprofile(request):
    if request.user:
        user=request.user
        receiverlist=receiver.objects.get(user=user)
        return render(request,'receiver/receiverprofile.html',{'receiverlist':receiverlist})

def receiverprofileupdate(request,receiver_id):
    if request.method=="POST":
        receiverlist1=receiver.objects.get(id=receiver_id)
        receiverlist1.fullname=request.POST['fullname']
        receiverlist1.blood=request.POST['blood']
        receiverlist1.gender=request.POST['gender']
        receiverlist1.job=request.POST['job']
        receiverlist1.phone=request.POST['phone']
        receiverlist1.email=request.POST['email']
        receiverlist1.address1=request.POST['address1']
        receiverlist1.address2=request.POST['address2']
        receiverlist1.post=request.POST['post']
        receiverlist1.district=request.POST['district']
        receiverlist1.country=request.POST['country']
        receiverlist1.pin=request.POST['pin']
        receiverlist1.weight=request.POST['weight']
        receiverlist1.bp=request.POST['bp']
        receiverlist1.prevreceive=request.POST['prevreceive']
        receiverlist1.save()
        return redirect("receiverprofile")
 



# login
stat=''
rol=''
def login(request):
    global stat
    global rol
    if request.method=='POST':
        username=request.POST.get('userName')
        password=request.POST.get('password')
        print(password)

        user= authenticate(username=username,password=password)
        print("Hi",user)


        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            u_name=i['username']
            print(u_name)
            id=i['id']

            ddon=donor.objects.filter(user_id=id).values()
            print("donorData==>",ddon)
            for i in ddon:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)


            drec=receiver.objects.filter(user_id=id).values()
            print("receiverData==>",drec)
            for i in drec:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)

            if user is not None and rol=='donor' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('donordashboard')
            
            elif user is not None and rol=='receiver' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('receiverdashboard')  


            elif username=="admin" and password=='admin1212':
                auth_login(request,user)
                return redirect('admindashboard')        

            else:pass

        else:
            messages.info(request,'Invalid Credentials')  
            return redirect('login') 

    else:
        return render(request,'common/login.html')     

# Create your views here.
