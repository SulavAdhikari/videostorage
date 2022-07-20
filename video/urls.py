from django.urls import path

from .views import (
    FileUploadView, 
    AllVideosListView,
    FilterVideos,
)

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('list/', AllVideosListView.as_view()),
    path('search/', FilterVideos.as_view()),
]