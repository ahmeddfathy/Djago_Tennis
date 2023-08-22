from django.db import models

# Create your models here.

class FirstSection(models.Model):
    one = models.CharField(max_length=250, null=True , blank=True)
    two = models.CharField(max_length=250, null=True , blank=True)
    three = models.CharField(max_length=250, null=True , blank=True)
    f_img = models.ImageField(upload_to="photos", null=True , blank=True)
    s_img = models.ImageField(upload_to="photos", null=True , blank=True)
    fo_img = models.ImageField(upload_to="photos", null=True , blank=True)
    fi_img = models.ImageField(upload_to="photos", null=True , blank=True)
    si_img = models.ImageField(upload_to="photos", null=True , blank=True)
    
    
 
    
class SecondSection(models.Model):
    one = models.CharField(max_length=250, null=True , blank=True)
    two = models.CharField(max_length=250, null=True , blank=True)
    three = models.CharField(max_length=250, null=True , blank=True)
    four = models.CharField(max_length=250, null=True , blank=True)
    f_img = models.ImageField(upload_to="photos", null=True , blank=True)
  
class ThirdSection(models.Model):
    one = models.CharField(max_length=250, null=True , blank=True)

    f_img = models.ImageField(upload_to="photos", null=True , blank=True)
    s_img = models.ImageField(upload_to="photos", null=True , blank=True)
    t_img = models.ImageField(upload_to="photos", null=True , blank=True)
    fo_img = models.ImageField(upload_to="photos", null=True , blank=True)
  
  
    
class FourthSection(models.Model):
    one = models.CharField(max_length=250, null=True , blank=True)
    two = models.CharField(max_length=250, null=True , blank=True)
    three = models.CharField(max_length=250, null=True , blank=True)
    four = models.CharField(max_length=250, null=True , blank=True)
    f_img = models.ImageField(upload_to="photos", null=True , blank=True)
    s_img = models.ImageField(upload_to="photos", null=True , blank=True)
    t_img = models.ImageField(upload_to="photos", null=True , blank=True)
    
    
class FifthSection(models.Model):
    one = models.CharField(max_length=250, null=True , blank=True)
    f_img = models.ImageField(upload_to="photos", null=True , blank=True)
    s_img = models.ImageField(upload_to="photos", null=True , blank=True)
    t_img = models.ImageField(upload_to="photos", null=True , blank=True)


class SixSection(models.Model):
    one = models.CharField(max_length=250, null=True , blank=True)
    f_img = models.ImageField(upload_to="photos", null=True , blank=True)
    s_img = models.ImageField(upload_to="photos", null=True , blank=True)
    two = models.CharField(max_length=250, null=True , blank=True)



class Video(models.Model):
    one = models.FileField(upload_to="video/%y")
  