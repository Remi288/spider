from django.contrib import admin
from spiderapp.models import Login

# Register your models here.


class LoginAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email']

admin.site.register(Login,LoginAdmin)