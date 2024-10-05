from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .models import Project
from .models import Main
from .models import Contact

from .forms import ContactForm


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact_obj = Contact.objects.create(name=name, email=email, message=message)
            contact_obj.save()

            messages.success(request, 'Your message has been sent successfully!')

            return render(request, "contact_success.html", {})
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {'form': form})

def blog_page(request):
    return render(request, "blog.html", {})