from django.urls import path
from .views import *
urlpatterns = [
    path('', Apiviews, name='Apiviews'),
    path('create/',views_item, name='views_item'),
    path('all/',afficher_all, name="afficher_all"),
    path('update/<int:pk>/', updates, name="updates"),
    path('delete/<int:pk>', delete, name="delete")

]
