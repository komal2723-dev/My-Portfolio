from django.contrib import admin
from .models import Project, Contactform
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['id', 'title']

@admin.register(Contactform)
class ContactFormAdmin(admin.ModelAdmin):
	list_display = ['id', 'full_name','created_at']