from django.urls import path
from . import views
urlpatterns = [
    path('notes/',views.NoteListCreate.as_view()),
    path('notes/delete/<int:pk>',views.NoteDelete.as_view())
]


