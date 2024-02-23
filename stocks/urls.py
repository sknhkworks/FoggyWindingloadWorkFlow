from django.contrib import admin
from django.urls import path

from stocks import views
from stocks import views_s
from stocks.views_s import parts
from stocks.views_s.parts import parts_new

    #path('/', views.top, name='top'),
urlpatterns = [
    path("new/", views.stocks_new, name="stocks_new"),
    path("<int:stock_id>/", views.stocks_detail, name="stocks_detail"),
    path("<int:stock_id>/edit/", views.stocks_edit, name="stocks_edit"),

    path("pnew/", views_s.parts.parts_new, name="parts_new"),

]
