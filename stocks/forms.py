from django import forms

from stocks.models import Stocks
from stocks.models import Parts

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ('title', 'code', 'description')

class PartForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = ('code', 'name', 'sizeType', 'created_by')
