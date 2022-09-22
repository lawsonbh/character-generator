from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class OwnerMixin():
    def get_queryset(self):
        #Override default query set to return only active user
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

class OwnerEditMixin():
    #because Antonio's book told me to : )
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerEgoMixin(OwnerMixin):
    model = Ego
    fields = ['cog','inte','ref','sav','som','wil','morph','items','user']
    success_url = reverse_lazy('manage_egos_list')

class OwnerEgoEditMixin(OwnerEgoMixin, OwnerEditMixin):
    template_name = 'character_generator/templates/form.html'

class ManageEgoListView(OwnerEgoMixin, ListView):
    template_name = 'character_generator/templates/list.html'

class EgoCreateView(OwnerEgoEditMixin, CreateView):
    pass

class EgoUpdateView(OwnerEgoEditMixin, UpdateView):
    pass

class EgoDeleteView(OwnerEgoMixin, DeleteView):
    tempalte_name = 'character_generator/templates/delete.html'