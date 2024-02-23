from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stocks.models import Stocks
from stocks.forms import StockForm

# Create your views here.
def top(request):
    stocks = Stocks.objects.all()
    context = { "stocks": stocks }
    return render(request, "stocks/top.html",context)

