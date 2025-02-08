from django import forms
from . models import Contactform
class ContactForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, required=True, label="Full Name", widget=forms.TextInput(attrs={'placeholder':'Enter your full name...','class':'form-control', 'id':'exampleInputEmail1', 'type':'text','autocomplete':'off', 'autocorrect':"off", 'autocapitalize':"off"}))
    email_address = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your Email...', 'class':"form-control", 'id':"exampleInputEmail1", 'type':"email",'autocomplete':'off', 'autocorrect':"off", 'autocapitalize':"off"}))
    subject = forms.CharField(max_length=200, required=True, label="Subject", widget=forms.TextInput(attrs={'placeholder': 'Enter Subject...', 'class':"form-control", 'id':"exampleInputSubject1", 'type':"text",'autocomplete':'off', 'autocorrect':"off", 'autocapitalize':"off"}))
    message = forms.CharField(required=True, label="Message",widget=forms.Textarea(attrs={'rows': 5, 'cols': 30, 'placeholder': 'Enter Message...', 'class':"form-control", 'id':"exampleFormControlTextarea1",'autocomplete':'off', 'autocorrect':"off", 'autocapitalize':"off"}))
    class Meta:
        model = Contactform
        fields = ['full_name','email_address','subject','message']
