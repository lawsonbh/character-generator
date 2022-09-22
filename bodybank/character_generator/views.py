from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
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
            return redirect('thanks')
            
    else:
        form = EgoForm()

    return render(request, 'ego.html', {'form': form})

def say_thanks(request):
    return render(request, 'thanks.html')

class EgoUpdateView(UpdateView):
    model = Ego
    fields = ['cog','inte','ref','sav','som','wil','morph','items','user']
    template_name_suffix = '_update_form'

    def get_queryset(self):
        # Override default query set to return only active user
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)
