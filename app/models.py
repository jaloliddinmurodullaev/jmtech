from uuid import uuid4
from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    technology = models.CharField(max_length=300)
    link = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0, null=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    likes = models.BigIntegerField(default=0, null=True)
    views = models.BigIntegerField(default=0, null=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Main(models.Model):
    image = models.URLField()
    github = models.URLField()
    linkedin = models.URLField()
    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField()
    about = models.TextField() 
    views = models.BigIntegerField(default=0, null=True)

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name

# class Experience(models.Model):
#     company = models.CharField(max_length=100)
#     position = models.CharField(max_length=200)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     description = models.TextField()

# class Resume(models.Model):
#     firstname = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     description = models.TextField()
#     about = models.TextField()
    