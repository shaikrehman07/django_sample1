import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'generator/home.html')


def password(request):

    characters = []
    generatedPass = ''
    length = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("numbers"):
        characters.extend((list('1234567890')))

    if request.GET.get("special"):
        characters.extend((list('!@#$%&')))

    if request.GET.get("lowercase"):
        characters.extend((list('abcdefghijklmnopqrstuvwxyz')))

    for i in range(length):
        generatedPass += random.choice(characters)

    return render(request,'generator/password.html',{'password':generatedPass})
