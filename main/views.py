from django.shortcuts import render, redirect
import re
from .models import *


def index(request):
    is_user_authenticated = request.user.is_authenticated
    return render(request, 'index.html', {"admin": is_user_authenticated})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        email_or_phone = request.POST['email']
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        if re.search(email_pattern, email_or_phone):
            Message.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                text=request.POST['text'],
            )
        else:
            Message.objects.create(
                name=request.POST['name'],
                phone_number=request.POST['email'],
                text=request.POST['text'],
            )

        return redirect("/contact/")

    return render(request, 'contact.html')

def messages(request):
    if request.user.is_authenticated:
        content = {
            "messages": Message.objects.all()
        }
        return render(request, 'messages.html', content)
    else:
        return redirect("/")