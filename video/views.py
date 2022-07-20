from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response 
from moviepy.editor import VideoFileClip

from videostorage.settings import UPLOAD_LIMIT
from .models import Video

# Create your views here.
class FileUploadView(views.APIView):
    
    def calculate_cost(self, video, clip):
        cost=0
        if video.size < 500*1024*1024:
            cost += 5
        else:
            cost+=12.5
        if clip.duration > (6*60)+18:
            cost+=20
        return cost


    def post(self, request):
        video = request.FILES['video']
        if video.name.endswith('.mp4') or video.name.endswith('.mkv'):
            
            clip =  VideoFileClip(video.temporary_file_path())
            duration = clip.duration
            
            if duration > 10*60:
                return Response({
                'message':'video exceeds length limit'
                }, status=400)
            print(video.size)
            if video.size > UPLOAD_LIMIT:
                return Response({
                'message':'file is too big'
            }, status=400)

            cost = self.calculate_cost(video, clip)        
            
            obj = Video(title=video.name,video=video, size=video.size, cost=cost)

            
            obj.save()


            return Response({
                'message':'file uploaded'
            }, status=201)
        else:
            return Response({
                'message':'invalid file type'
            }, status=400)
        