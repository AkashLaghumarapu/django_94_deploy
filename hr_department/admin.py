from django.contrib import admin
from hr_department.models import emp_table
# Register your models here.
class emp_admin(admin.ModelAdmin):
    list_display=['eid','emp_name','emp_salary']
    ordering=['eid']
admin.site.register(emp_table,emp_admin)