from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('example/', example),
    path('line/', line),
    path('pie/', pie),
    path('XY/', XY),
    path('map/', map),
    path('candlesticks/', candlesticks),
    path('stock/', stock),
    path('pyramid/', pyramid),
    path('miscellaneous/', miscellaneous)
]