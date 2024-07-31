from django.urls import path

from .views import about_page
from .views import resume_page
from .views import projects_page
from .views import contact_page
from .views import blog_page

urlpatterns = [
    path('', about_page),
    path('resume/', resume_page),
    path('projects/', projects_page, name='projects_page'),
    path('contact/', contact_page),
    path('blog/', blog_page)
]