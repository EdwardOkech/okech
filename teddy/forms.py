from django import forms
from teddy.models import Portfolio, Contact
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact




    
        
