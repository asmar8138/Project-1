from django.urls import path
from . import views

urlpatterns = [
    path('index',views.function),
    path('html',views.function1),
    path('',views.function2)
]