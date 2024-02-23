from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stocks.models import Parts
from stocks.forms import PartForm

def parts_new(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
          part = form.save(commit=False)
          part.created_by = request.user
          part.save()
#          return redirect(stocks_detail, stock_id=stock.pk)
          return render(request, "stocks/part_done.html", {'form': form})
    else:
        form = PartForm()
    return render(request, "stocks/part_done.html", {'form': form})


