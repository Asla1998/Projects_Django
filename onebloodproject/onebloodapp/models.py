from django.db import models
from django.contrib.auth.models import User

class donor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255,blank=False,null=False)
    donor_img=models.ImageField(null=True,blank=True,upload_to="images/")
    blood = models.CharField(max_length=255,blank=False,null=False)
    dob = models.DateField()
    gender = models.CharField(max_length=255,blank=False,null=False)
    job = models.CharField(max_length=255,blank=False,null=False)
    phone = models.CharField(max_length=255,blank=False,null=False)
    email = models.CharField(max_length=255,blank=False,null=False)
    address1 = models.CharField(max_length=255,blank=False,null=False)
    address2 = models.CharField(max_length=255,blank=False,null=False)
    post = models.CharField(max_length=255,blank=False,null=False)
    district = models.CharField(max_length=255,blank=False,null=False)
    country = models.CharField(max_length=255,blank=False,null=False)
    pin = models.IntegerField()
    weight = models.CharField(max_length=255,blank=False,null=False)
    bp = models.CharField(max_length=255,blank=False,null=False)
    prevdonation = models.CharField(max_length=255,blank=False,null=False)
    status = models.CharField(max_length=255,blank=False,null=False)
    role = models.CharField(max_length=255,blank=False,null=False)
   





    def __str__(self):
        return self.email




class receiver(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255,blank=False,null=False)
    receiver_img=models.ImageField(null=True,blank=True,upload_to="images/")
    blood = models.CharField(max_length=255,blank=False,null=False)
    dob = models.DateField()
    gender = models.CharField(max_length=255,blank=False,null=False)
    job = models.CharField(max_length=255,blank=False,null=False)
    phone = models.CharField(max_length=255,blank=False,null=False)
    email = models.CharField(max_length=255,blank=False,null=False)
    address1 = models.CharField(max_length=255,blank=False,null=False)
    address2 = models.CharField(max_length=255,blank=False,null=False)
    post = models.CharField(max_length=255,blank=False,null=False)
    district = models.CharField(max_length=255,blank=False,null=False)
    country = models.CharField(max_length=255,blank=False,null=False)
    pin = models.IntegerField()
    weight = models.CharField(max_length=255,blank=False,null=False)
    bp = models.CharField(max_length=255,blank=False,null=False)
    prevreceive = models.CharField(max_length=255,blank=False,null=False)
    status = models.CharField(max_length=255,blank=False,null=False)
    role = models.CharField(max_length=255,blank=False,null=False)






    def __str__(self):
        return self.email     



class blood_req(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    donor_id=models.ForeignKey(donor,on_delete=models.CASCADE,related_name="donordetail")
    rec_id=models.ForeignKey(receiver,on_delete=models.CASCADE,related_name="receiverdetail")   
    status=models.CharField(max_length=255,blank=False,null=False) 


    def __str__(self):
        return self.status    



class blog(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    blog_img = models.ImageField(null=True,blank=True,upload_to="images/")
    description = models.CharField(max_length=255,blank=False,null=False)
    bloger_img = models.ImageField(null=True,blank=True,upload_to="images/")
    name = models.CharField(max_length=255,blank=False,null=False)
    date = models.DateField()
    status = models.CharField(max_length=255,blank=False,null=False)


    def __str__(self):
        return self.title   



# Create your models here.
