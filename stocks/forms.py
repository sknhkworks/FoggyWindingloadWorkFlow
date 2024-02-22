from django import forms

from stocks.models import Stocks

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ('title', 'code', 'description')


