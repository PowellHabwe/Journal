from django.urls import path
from . import views

urlpatterns = [
    path("journalpost/", views.JournalPostListCreate.as_view(), name="note-list"),
    path("journalpost/delete/<int:pk>/", views.JournalPostDelete.as_view(), name="delete-note"),
    path('journalpost/<int:pk>/', views.JournalPostRetrieveUpdateDestroy.as_view(), name='retrieve-update-destroy-journal'),

    path('journals/summary/', views.JournalPostSummaryView.as_view(), name='summary-journal'),

]
