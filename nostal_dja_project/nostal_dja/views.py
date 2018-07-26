from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm
from django.contrib.auth.decorators import login_required

#################### DECADES #################

# index - decades
def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostal_dja/decade_list.html', { 'decades': decades })

# show - decade
def decade_detail(request, pk):
    decade = Decade.objects.get(pk=pk)
    return render(request, 'nostal_dja/decade_detail.html', { 'decade': decade })

# create - decade
@login_required
def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostal_dja/decade_form.html', { 'form': form })

# update - decade
def decade_update(request, pk):
    decade = Decade.objects.get(id=pk)
    if request.method == 'POST':
        form = DecadeForm(request.POST, instance=artist)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=artist.pk)
    else:
        form = DecadeForm(instance=artist)
    return render(request, 'nostal_dja/decade_form.html', { 'form': form })

# delete - decade
@login_required
def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')

################### FADS #####################

# index - fads
def fads_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostal_dja/fad_list.html', { 'fads': fads })

# show - fads
def fads_detail(request, id):
    fad = Fad.objects.get(id=id)
    return render(request, 'nostal_dja/fad_detail.html', { 'fad': fad })

# create - fads
def fads_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fads_detail', id=fad.id)
    else:
        form = FadForm()
    return render(request, 'nostal_dja/decade_form.html', { 'form': form })

def fads_update(request, id):
    fad = Fad.object.get(id=id)
    if request.method == 'POST':
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            song = form.save()
            return redirect('fad_detail', id=fad.id)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostal_dja/fad_form.html', { 'form': form })

def fads_delete(request, id):
    Fad.objects.get(id=id).delete()
    return redirect('fads_list')