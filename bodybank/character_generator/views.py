from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import EgoForm, CharacterSheetForm
from .models import Ego, Morph, CharacterSheet
from django.contrib.auth.decorators import login_required


@login_required
def create_ego(request):
    if request.method == "POST":
        form = EgoForm(request.POST)
        if form.is_valid():
            ego = form.save(commit=False)
            ego.user = request.user
            ego.save()
            return redirect("list_egos")
    else:
        form = EgoForm()

    return render(request, "ego.html", {"form": form})


@login_required
def edit_ego(request, pk):
    ego = get_object_or_404(Ego, pk=pk)
    form = EgoForm(request.POST or None, instance=ego)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated Ego")
        return redirect("list_egos")
    return render(request, "ego_form.html", {"form": form})


@login_required
def list_user_egos(request):
    egos = Ego.objects.filter(user=request.user).all()
    return render(request, "ego_list.html", {"egos": egos})


@login_required
def delete_ego(request, pk):
    ego = get_object_or_404(Ego, pk=pk)

    if request.method == "POST":
        ego.delete()
        messages.success(request, "Deleted Ego")
        return redirect("list_egos")

    return render(request, "delete_ego.html", {"ego": ego})


def list_morphs(request):
    morphs = Morph.objects.all()
    return render(request, "morph_list.html", {"morphs": morphs})


def say_thanks(request):
    return render(request, "thanks.html")


@login_required
def create_character_sheet(request):
    if request.method == "POST":
        form = CharacterSheetForm(request.POST, user=request.user)
        if form.is_valid():
            character_sheet = form.save(commit=False)
            character_sheet.user = request.user
            character_sheet.save()
            return redirect("list_character_sheets")
    else:
        form = CharacterSheetForm(user=request.user)
    return render(request, "character_sheet.html", {"form": form})


@login_required
def edit_character_sheet(request, pk):
    character_sheet = get_object_or_404(CharacterSheet, pk=pk)
    form = CharacterSheetForm(request.POST or None, instance=character_sheet)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated Character Sheet")
        return redirect("list_character_sheets")
    return render(request, "character_sheet_form.html", {"form": form})


@login_required
def delete_character_sheet(request, pk):
    character_sheet = get_object_or_404(CharacterSheet, pk=pk)

    if request.method == "POST":
        character_sheet.delete()
        messages.success(request, "Deleted Character Sheet")
        return redirect("list_character_sheets")

    return render(
        request, "delete_character_sheet.html", {"character_sheet": character_sheet}
    )


@login_required
def list_user_character_sheets(request):
    character_sheets = CharacterSheet.objects.filter(user=request.user).all()
    return render(
        request, "character_sheet_list.html", {"character_sheets": character_sheets}
    )
