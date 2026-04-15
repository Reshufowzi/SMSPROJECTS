from django.contrib import admin
from .models import Department,Placementcell,Search
# Register your models here.

admin.site.register(Department)
admin.site.register(Placementcell)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('id','student_name',
                    'student_phonenumber',
                    'student_email',
                    'student_image')
admin.site.register(Search,SearchAdmin)
