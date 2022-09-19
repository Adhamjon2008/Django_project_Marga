import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.
def index(malumot):
    if 'qidirish' in malumot.POST:
        matn = str(malumot.POST.get('qidirish'))
        matn = matn.strip()
        izlash = Q(nomi__startswith=matn )| Q(manzil__startswith=matn )| Q(turi__nomi__startswith=matn )
        project = Project.objects.filter(izlash)
        return render(malumot,'index.html',{'proyekt':project})
    else:
        uzunlik = len(Project.objects.all())
        oxirgisi = uzunlik-2
        project = Project.objects.all()[oxirgisi:]
        return render(malumot,'index.html',{'proyekt':project})
def about(malumot):
    if 'qidirish' in malumot.POST:
        matn = str(malumot.POST.get('qidirish'))
        matn = matn.strip()
        izlash = Q(lavozim__startswith=matn )| Q(ism__startswith=matn )
        xodimlar = Xodimlar.objects.filter(izlash)
        return render(malumot,'about.html',{'xodim':xodimlar})
    else:
        xodimlar = Xodimlar.objects.all()
        return render(malumot,'about.html',{'xodim':xodimlar})
def blog(malumot):
    if 'qidirish' in malumot.POST:
        matn = str(malumot.POST.get('qidirish'))
        matn = matn.strip()
        izlash = Q(nomi__startswith=matn )| Q(manzil__startswith=matn )| Q(turi__nomi__startswith=matn )
        project = Project.objects.filter(izlash)
        return render(malumot,'blog.html',{'proyekt':project})
    else:
        project = Project.objects.all()
        return render(malumot,'blog.html',{'proyekt':project})
def contact(malumot):

    if malumot.method =="POST":
        ism = malumot.POST.get('name')
        fam = malumot.POST.get('surename')
        email = malumot.POST.get('email')
        malumot = malumot.POST.get('text')
        vaqt = datetime.datetime.now()
        Sendlar(ism=ism,fam=fam,mail=email,matn=malumot,vaqt=vaqt).save()
    return render(malumot,'contact.html')
def main(malumot):
    uzunlik = len(Project.objects.all())
    oxirgisi = uzunlik - 2
    project = Project.objects.all()[oxirgisi:]
    return render(malumot,'main.html',{'proyekt':project})
def projects(malumot):
    if 'qidirish' in malumot.POST:
        matn = str(malumot.POST.get('qidirish'))
        matn = matn.strip()
        izlash = Q(nomi__startswith=matn) | Q(manzil__startswith=matn) | Q(turi__nomi__startswith=matn)
        project = Project.objects.filter(izlash)
        return render(malumot, 'project.html', {'proyekt': project})
    else:
        project = Project.objects.all()
        return render(malumot,'project.html',{'proyekt':project})
def services(malumot):
    if 'qidirish' in malumot.POST:
        matn = str(malumot.POST.get('qidirish'))
        matn = matn.strip()
        izlash = Q(nomi__startswith=matn) | Q(manzil__startswith=matn) | Q(turi__nomi__startswith=matn)
        project = Project.objects.filter(izlash)
        return render(malumot, 'services.html', {'proyekt': project})
    else:
        uzunlik = len(Project.objects.all())
        oxirgisi = uzunlik-2
        project = Project.objects.all()[oxirgisi:]
        return render(malumot,'services.html',{'proyekt':project})
def single(malumot):
    return render(malumot,'single.html')