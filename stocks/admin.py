from django.contrib import admin
from stocks.models import Stocks
from stocks.models import Parts
from stocks.models import Shelfs

# Register your models here.
admin.site.register(Stocks)
admin.site.register(Parts)
admin.site.register(Shelfs)
