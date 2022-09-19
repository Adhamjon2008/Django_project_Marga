from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminType)

class AdminProject(admin.ModelAdmin):
    list_display = ['id', 'nomi','turi','rasm','manzil','vaqt']

admin.site.register(Project, AdminProject)

class AdminS(admin.ModelAdmin):
    list_display = ['id', 'ism','fam','mail','matn','vaqt']

admin.site.register(Sendlar, AdminS)

class AdminX(admin.ModelAdmin):
    list_display = ['id','lavozim','ism','rasm','malumot']

admin.site.register(Xodimlar,AdminX)