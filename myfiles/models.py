from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi
class Project(models.Model):
    nomi = models.CharField(max_length=30)
    manzil = models.CharField(max_length=40)
    rasm = models.ImageField(upload_to='media')
    turi = models.ForeignKey(Type,on_delete=models.CASCADE)
    vaqt = models.DateTimeField(auto_now=True)

class Xodimlar(models.Model):
    rasm = models.ImageField(upload_to='media')
    lavozim = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    malumot = models.TextField()

class Sendlar(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    matn = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)
