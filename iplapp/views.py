from django.shortcuts import render
from iplapp import forms
from django.shortcuts import redirect
from .models import Team

# Create your views here.
def home_view(request):
    return render(request, 'iplapp/home.html')


def add_team_view(request):
    if request.method == 'POST':
        form = forms.ModelTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display')
    else:
        form = forms.ModelTeamForm()
    return render(request, 'iplapp/add.html', context = {'form' : form})


def display_team_view(request):
    data = Team.objects.all()
    return render(request, 'iplapp/display.html', context = {'team_list' : data})


def update_team_view(request, id):
    data = Team.objects.get(id = id)
    if request.method == 'POST':
        form = forms.ModelTeamForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect('/display')
    else:
        form = forms.ModelTeamForm(instance=data)
    return render(request, 'iplapp/update.html', context = {'form' : form})

def delete_team_view(request, id):
    data = Team.objects.get(id = id)
    data.delete()
    return redirect('/display')
    return render(request, 'iplapp/display.html')