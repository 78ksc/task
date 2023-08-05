from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Job_post(models.Model):
    job_titel = models.CharField(max_length=20, null=True ,blank=True)
    job_desc = models.TextField(blank=True)
    last_date = models.DateTimeField(blank=True)
    vacancy = models.IntegerField( null=True ,blank=True)
    experience_required = models.IntegerField(null=True ,blank=True)
    
class Intern_post(models.Model):
    i_titel = models.CharField(max_length=20, null=True ,blank=True)
    i_desc = models.TextField(blank=True)
    last_date = models.DateTimeField(blank=True)
    vacancy = models.IntegerField( null=True ,blank=True)
    # experience_required = models.IntegerField(null=True ,blank=True)
    
class X_post(models.Model):
    job_titel = models.CharField(max_length=20, null=True ,blank=True)
    job_desc = models.TextField(blank=True)
    last_date = models.DateTimeField(blank=True)
    # vacancy = models.IntegerField( null=True ,blank=True)
    experience_required = models.IntegerField(null=True ,blank=True)
    change = models.BooleanField(default=False)
    
class Japp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    job = models.ForeignKey(Job_post,on_delete=models.CASCADE ,null=True)

    
class Xapp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    xchange = models.ForeignKey(X_post,on_delete=models.CASCADE ,null=True)
    
class Iapp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    internship = models.ForeignKey(Intern_post,on_delete=models.CASCADE ,null=True)
