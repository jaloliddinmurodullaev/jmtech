from django.shortcuts import render

from .models import Project


def about_page(request):
    print("SHOTTA")
    return render(request, "about.html", {})

def projects_page(request):
    projects = Project.objects.all()
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