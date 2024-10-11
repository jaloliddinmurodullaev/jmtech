from django.contrib import admin

from .models import Project, Blog, Contact

admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Contact)
