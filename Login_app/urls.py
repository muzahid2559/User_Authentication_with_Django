from django.urls import path
from CRUD import views

urlpatterns = [

    path('', views.index, name='index'),
]
