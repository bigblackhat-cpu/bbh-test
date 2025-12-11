from django.urls import path
from .views import ListHostRent

urlpatterns =[
    path('house_rent/',ListHostRent.as_view(),name='house_rent')
]