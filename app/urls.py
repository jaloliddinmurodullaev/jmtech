from django.urls import path

from .views import about_page
from .views import resume_page
from .views import projects_page
from .views import contact_page
from .views import blog_page
from .views import download_resume

urlpatterns = [
    path('', about_page, name='home'),
    path('resume/', resume_page, name='resume_page'),
    path('projects/', projects_page, name='projects_page'),
    path('contact/', contact_page, name='contact_page'),
    path('blog/', blog_page, name='blog_page'),
    path('blog/<int:id>/', blog_page, name='blog_detail_page'),
    path('download-resume/', download_resume, name='download_resume')
]

from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

handler404 = 'main.urls.custom_404'
