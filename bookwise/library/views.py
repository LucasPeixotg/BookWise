from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_library(request):
    return render(request, "home_library.html", {})

@login_required
def add_library(request):
    if request.method == "POST":
        pass

    return render(request, 'create_library.html', {})