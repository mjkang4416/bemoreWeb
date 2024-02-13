from django.contrib import admin

# Register your models here.
from accounts.models import userList

admin.site.register(userList)