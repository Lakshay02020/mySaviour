from django.contrib import admin
from .models import Year, Branch, Courses, Document_type, Documents, Wifi
# Register your models here.

admin.site.register(Wifi)
admin.site.register(Year)
admin.site.register(Branch)
admin.site.register(Courses)
admin.site.register(Document_type)
admin.site.register(Documents)
