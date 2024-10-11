from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse


from weasyprint import HTML

from .models import Project
from .models import Main
from .models import Contact
from .models import Blog

from .forms import ContactForm


def about_page(request):
    views = Main.objects.get_or_create(id=1)
    views[0].views += 1
    views[0].save()
    return render(request, "about.html", {})

def projects_page(request, id=None):
    if id is None:
        projects = Project.objects.all()            
        return render(request, "projects.html", {"projects": projects})
    else:
        try:
            project = Project.objects.get(id=id)
            project.views += 1
            project.save()
            return render(request, "project_detail.html", {"project": project})
        except Exception as e:
            return render(request, '404.html')

def resume_page(request):
    return render(request, "resume.html", {})

def download_resume(request):
    html_string = render_to_string('resume_pdf.html')
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="jaloliddinmurodullaev.pdf"'  # Set your desired filename
    return response

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

def blog_page(request, id=None):
    if id is None:
        blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
        return render(request, "blog.html", {'blogs': blogs})
    else:
        try:
            blog = Blog.objects.get(id=id)
            return render(request, "blog_detail.html", {'blog': blog})
        except Exception as exc:
            print(str(exc))
            return render(request, '404.html')