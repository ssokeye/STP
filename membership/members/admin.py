from django.contrib import admin

# Register your models here.
from .models import Members
from .models import Departments,Training,Member_Department

admin.site.register(Members)
admin.site.register(Departments)
admin.site.register(Training)
admin.site.register(Member_Department)