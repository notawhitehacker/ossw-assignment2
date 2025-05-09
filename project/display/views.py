from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Proj
from .forms import CreditForm

def index(request) :
    projects = Proj.objects.all()
    return render(request, 'display/proj_list.html', {'projects' : projects})

def display_proj(request, name): 
    project = get_object_or_404(Proj, name=name)
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            project.credit = form.cleaned_data['credit']
            project.save()
            return redirect('proj_detail', name=project.name)
    else:
        form = CreditForm()
    return render(request, 'display/proj_detail.html', {'project': project, 'form': form})    
