from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response 
from moviepy.editor import VideoFileClip

from videostorage.settings import UPLOAD_LIMIT
from .serializers import Videoserializer
from .models import Video

# Create your views here.
class FileUploadView(views.APIView):
    
    serializer_class = Videoserializer
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
        