from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Project, Blog, Contact

admin.site.register(Project)
# admin.site.register(Blog)
admin.site.register(Contact)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
