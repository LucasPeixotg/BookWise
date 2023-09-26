from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def error(request, code, message):
    return render(request, 'error.html', {'code': code, 'message': message})