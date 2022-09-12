from django.http import HttpResponse
from django.shortcuts import render
from .forms import EgoForm

def index(request):
    return HttpResponse("Welcome to the Body Bank!")

def get_ego(request):
    if request.method == 'POST':
        form = EgoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = EgoForm()

    return render(request, 'ego.html', {'form': form})
