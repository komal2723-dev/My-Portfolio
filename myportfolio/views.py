from django.shortcuts import render,redirect
from . forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import os
from django.http import FileResponse, Http404
# Create your views here.
def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		# send email notification

			send_mail(
			subject=f"New Message: {form.cleaned_data['subject']}",
			message=f"From: {form.cleaned_data['full_name']} \nEmail:<{form.cleaned_data['email_address']}>\n\n{form.cleaned_data['message']}",
			from_email= form.cleaned_data["email_address"],
			recipient_list=[settings.EMAIL_HOST_USER],
			fail_silently=False,
				)
			messages.success(request,"Message sent successfully")
			return redirect('home')
		else:
			messages.error(request,"Error sending message")
			return redirect('home')
	else:
		form = ContactForm()
	return render(request,'myportfolio/home.html',{'form':form})

