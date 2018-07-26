from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm

#################### DECADES #################

# index - decades
def decade_list(request):
    decades = Decade.objects.all()
    return render(requst, 'nostal_dja/decade_list.html', { 'decades': decades })

# show - decade
def decade_detail(request, pk):
    decade = Decade.objects.get(pk=pk)
    return render(request, 'nostal_dja/decade_detail.html', { 'decade': decade })

# create - decade
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
    

# delete - decade

################### FADS #####################

# index - fads
def fads_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostal_dja/fad_list.html', { 'fads': fads })

# show - fads
def fads_detail(request, id):
    fad = Fad.objects.get(id=id)
    return render(request, 'nostal_dja/fads_detail.html', { 'fad': fad })

# create - fads
def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', id=fad.id)
    else:
        form = FadForm()
    return render(request, 'nostal_dja/decade_form.html', { 'form': form })
