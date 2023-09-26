from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LibraryForm
from .models import Library

from website.views import error

@login_required
def my_libraries(request):
    libraries = Library.objects.all().filter(owner=request.user)
    
    return render(request, "my_libraries.html", {'libraries': libraries})

@login_required
def add_library(request):
    if request.method == "POST":
        form = LibraryForm(request.POST)
        
        if form.is_valid():
            library = form.save(commit=False)
            library.owner = request.user
            library.save()
            
            return redirect('home_library')
    else:
        form = LibraryForm()

    return render(request, 'create_library.html', { 'form': form })

@login_required
def home_library(request, id):
    try:
        library = Library.objects.get(id=id)
    except:
        return error(request, 404, "Oops! Not Found")
    
    if library.owner != request.user:
        # not editable
        #return render(request, )
        pass
        
    return render(request, 'home_library.html', {'library' : library})
    
    