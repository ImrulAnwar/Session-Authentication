

from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteView.as_view(), name='all_notes'),
]