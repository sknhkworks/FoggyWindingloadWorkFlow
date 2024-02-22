from django.contrib import admin
from django.urls import path

from stocks import views

urlpatterns = [
    path("new/", views.stocks_new, name="stocks_new"),
    path("<int:stock_id>/", views.stocks_detail, name="stocks_detail"),
    path("<int:stock_id>/edit/", views.stocks_edit, name="stocks_edit"),
]
