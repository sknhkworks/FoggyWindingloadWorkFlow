from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stocks.models import Stocks
from stocks.forms import StockForm

def stocks_new(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
          stock = form.save(commit=False)
          stock.created_by = request.user
          stock.save()
          return redirect(stocks_detail, stock_id=stock.pk)
    else:
        form = StockForm()
    return render(request, "stocks/stock_new.html", {'form': form})

def stocks_edit(request, stock_id):
    stock = get_object_or_404(Stocks, pk=stock_id)
    if stock.created_by_id != request.user.id:
        return HpptResponseForbidden("not allowed")

    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stocks_detail', stock_id=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, "stocks/stock_edit.html", {'form': form})

def stocks_detail(request, stock_id):
    stock = get_object_or_404(Stocks, pk=stock_id)
    return render(request, "stocks/stock_detail.html",
            { 'stock' : stock })

