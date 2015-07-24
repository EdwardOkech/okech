from django.shortcuts import get_object_or_404, render_to_response,render, Http404
from teddy.models import Portfolio
from django.contrib.flatpages import views
from teddy.forms import *
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, 'teddy/index.html',)

def about(request):
    return render(request, 'teddy/about.html',)

def projects(request):
    return render(request, 'teddy/projects.html',)

def hobbies(request):
    return render(request, 'teddy/hobbies.html',)


def hire(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject =form.cleaned_data['subject']
            message = form.cleaned_data['message']
            address = form.cleaned_data['address']
            sender = form.cleaned_data['sender']

            recipients = ['okechjobs@gmail.com']
##            send_mail(subject,message,address,sender,recipients)
            return HttpResponseRedirect('/teddy/thanks/')
    else:
        form = ContactForm()
    return render(request, 'teddy/hire.html', {'form':form})

def thanks(request):
    return render(request, 'teddy/thanks.html',)
