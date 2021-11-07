from django.contrib import admin
from core.models import Student,Teacher,Book,BookIssue,Event,Due,Contact

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Book)
admin.site.register(BookIssue)
admin.site.register(Event)
admin.site.register(Due)
admin.site.register(Contact)
