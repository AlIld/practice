from django.urls import path, re_path

from animals.views import cat_view
from animals.views import dog_view
from animals.views import fox_view


app_name = 'animals'

urlpatterns = [
    path('cat/', cat_view, name="cat"),
    path('dog/', dog_view, name="dog"),
    path('fox/', fox_view, name="fox"),
]