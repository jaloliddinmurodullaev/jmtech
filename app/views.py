from django.shortcuts import render

from .models import Project
from .models import Main


def about_page(request):
    # print("SHOTTA")
    views = Main.objects.get_or_create(id=1)
    views[0].views += 1
    views[0].save()
    return render(request, "about.html", {})

def projects_page(request):
    projects = Project.objects.all()

    for proj in projects:
        proj.views += 1
        proj.save()
        
    context = {
        "projects": projects
    }
    return render(request, "projects.html", context)

def resume_page(request):
    return render(request, "resume.html", {})

def contact_page(request):
    return render(request, "contact.html", {})

def blog_page(request):
    return render(request, "blog.html", {})