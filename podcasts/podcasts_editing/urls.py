from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('podcast', views.podcast, name='podcast'),
    path('podcast/edit', views.edit, name='edits'),
    path('photo/<str:name>', views.photo, name='photo'),
    path('audio/<str:name>', views.audio, name='audio'),
]
