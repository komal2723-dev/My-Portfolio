from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)


class Contactform(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"Message from {self.full_name}"