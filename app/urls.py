from django.urls import path

from .views import about_page
from .views import resume_page
from .views import projects_page
from .views import contact_page
from .views import blog_page
from .views import download_resume
from .views import post_blog

urlpatterns = [
    path('', about_page, name='home'),
    path('post/', post_blog, name='post_blog'),
    path('resume/', resume_page, name='resume_page'),
    path('projects/', projects_page, name='projects_page'),
    # path('projects/<int:id>', projects_page, name='project_detail_page'),
    path('contact/', contact_page, name='contact_page'),
    path('blog/', blog_page, name='blog_page'),
    path('blog/<slug:slug>/', blog_page, name='blog_detail_page'),
    path('download-resume/', download_resume, name='download_resume')
]
