from django.contrib import admin

# Register your models here.
from .models import Member
from .models import Department,Training,Member_Department

admin.site.register(Member)
admin.site.register(Department)
admin.site.register(Training)
admin.site.register(Member_Department)