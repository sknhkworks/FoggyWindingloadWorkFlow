from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stocks.models import Parts
from stocks.forms import PartForm

def parts_browse(request):
    parts = Parts.objects.all()
    context = { "parts": parts }
    return render(request, "parts/parts_browse.html",context)

def parts_new(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
          part = form.save(commit=False)
          part.created_by = request.user
          part.save()
          return redirect(parts_detail, part_id=part.pk)
    else:
        form = PartForm()

    #return render(request, "stocks/part_new.html", {'form': form})
    return render(request, "parts/parts_new.html", {'form': form})

def parts_detail(request, part_id):
    part = get_object_or_404(Parts, pk=part_id)
    return render(request, "parts/parts_detail.html",
            { 'part' : part })


