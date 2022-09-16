from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EgoForm

def index(request):
    return HttpResponse("Welcome to the Body Bank!")

def get_ego(request):
    if request.method == 'POST':
        form = EgoForm(request.POST)
        if form.is_valid():
            ego = form.save(commit=False)
            ego.user = request.user
            ego.save()
            return redirect('thanks')
            
    else:
        form = EgoForm()

    return render(request, 'ego.html', {'form': form})

def say_thanks(request):
    return render(request, 'thanks.html')
