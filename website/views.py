from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def contact(request):
    return render(request, 'website/contact.html')
