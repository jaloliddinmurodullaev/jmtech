from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    technology = models.CharField(max_length=300)
    link = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=300)
    desctiption = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    likes = models.BigIntegerField(default=0, null=True)
    views = models.BigIntegerField(default=0, null=True)

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
    