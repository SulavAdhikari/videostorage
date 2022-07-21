from django.urls import path

from .views import (
    FileUploadView, 
    AllVideosListView,
    FilterVideos,
    CostCalculator,
)

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('listvideos/', AllVideosListView.as_view()),
    path('search/', FilterVideos.as_view()),
    path('cost/', CostCalculator.as_view()),
]