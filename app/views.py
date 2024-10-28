import requests
import markdown

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings

# from weasyprint import HTML

from .models import Project
from .models import Main
from .models import Contact
from .models import Blog

from .forms import ContactForm
from .forms import BlogForm


def about_page(request):
    views = Main.objects.get_or_create(id=1)
    views[0].views += 1
    views[0].save()
    return render(request, "about.html", {})

def projects_page(request, id=None):
    if id is None:
        projects = Project.objects.filter(is_active=True)  
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
    response = {
        "status": 'OK'
    }
    # html_string = render_to_string('resume_pdf.html')
    # html = HTML(string=html_string)
    # pdf = html.write_pdf()

    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="jaloliddinmurodullaev.pdf"'  # Set your desired filename
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

            telegram_message = f"New Message from jaloliddin.com:\n\nName: {name}\nEmail: {email}\n\nMessage: {message}"

            BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
            CHAT_ID=settings.TELEGRAM_CHAT_ID

            telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

            requests.post(telegram_url, data={'chat_id': CHAT_ID, 'text': telegram_message})

            messages.success(request, 'Your message has been sent successfully!')

            return render(request, "contact_success.html", {})
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {'form': form})

def post_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs_page')
    else:
        form = BlogForm()
    return render(request, 'post_blog.html', {'form': form})

def blog_page(request, id=None):
    if id is None:
        try:
            blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
            return render(request, "blog.html", {'blogs': blogs})
        except Exception as e:
            print(str(e))
    else:
        try:
            md = markdown.Markdown(extensions=["fenced_code"])
            blog = Blog.objects.get(id=id)
            blog.content = md.convert(blog.content)
            return render(request, "blog_detail.html", {'blog': blog})
        except Exception as exc:
            print(str(exc))
            return render(request, '404.html')