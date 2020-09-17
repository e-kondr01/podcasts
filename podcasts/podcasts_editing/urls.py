from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('podcast', views.podcast, name='podcast'),
    path('podcast/edit', views.edit, name='edits'),
    path('photo/<str:id>', views.photo, name='photo'),
    path('audio/<str:id>', views.audio, name='audio'),
]
