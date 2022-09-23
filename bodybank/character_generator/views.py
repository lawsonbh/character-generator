from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import EgoForm
from .models import Ego
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Welcome to the Body Bank!")

@login_required
def get_ego(request):
    if request.method == 'POST':
        form = EgoForm(request.POST)
        if form.is_valid():
            ego = form.save(commit=False)
            ego.user = request.user
            ego.save()
            return redirect('manage_egos_list')
            
    else:
        form = EgoForm()

    return render(request, 'ego.html', {'form': form})

@login_required
def update_ego(request, pk):
    ego = get_object_or_404(Ego, pk=pk)
    form = EgoForm(request.POST or None, instance=ego)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated Ego')
        return redirect('manage_egos_list')
    return render(request, 'form.html', {'form':form})

@login_required
def list_user_egos(request):
    egos = Ego.objects.all()
    return render(request, 'list.html', {'egos':egos})

@login_required
def ego_delete(request, pk):
    ego = get_object_or_404(Ego, pk=pk)

    if request.method == 'POST':
        ego.delete()
        messages.success(request, 'Deleted Ego')
        return redirect('manage_egos_list')
    
    return render(request, 'delete.html', {'ego':ego})

def say_thanks(request):
    return render(request, 'thanks.html')