from django.urls import path
from .views import *
urlpatterns = [
    path('all/',afficher_all, name="afficher_all"),
    path('create/',views_item, name='views_item'),
    path('update/<int:pk>/', updates, name="updates"),
    path('delete/<int:pk>', delete, name="delete"),
    path('sing/', sing, name="sing"),
    path('all_to',all_to, name="all_to"),
    path('loging/',loging,name="loging"),

]
