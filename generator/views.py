from django.shortcuts import render
from django.http import HttpResponse
import string, random

def home(request):
    return render(request, 'generator/home.html')
    
def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = string.ascii_lowercase

    if request.GET.get('uppercase'): characters += string.ascii_uppercase
    if request.GET.get('numbers'): characters += string.digits
    if request.GET.get('special'): characters += "!@#$%^&*()"

    length = int(request.GET.get('length', 12))
    thepassword = ''.join(random.choices(characters, k=length))
    return render(request, 'generator/password.html', {"password": thepassword})