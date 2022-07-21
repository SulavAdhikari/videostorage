from telnetlib import STATUS
from rest_framework.generics import ListAPIView
from rest_framework import views
from rest_framework.response import Response 

from videostorage.settings import UPLOAD_LIMIT
from .serializers import Videoserializer, ListAllSerializer
from .models import Video

# HTTP endpoints for /upload
class FileUploadView(views.APIView):
    
    serializer_class = Videoserializer
    
    # HTTP POST endpoint to upload and validate video
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

# HTTP endpoints for /listvideos
class AllVideosListView(ListAPIView):
    model = Video
    serializer_class = ListAllSerializer
    queryset = Video.objects.all()

# HTTP endpoints for /search
class FilterVideos(views.APIView):

    serializer_class = ListAllSerializer

    # Returns search results
    def get(self, request):
        data = request.GET
        title = data.get('title')
        obj = Video.objects.filter(title__contains=title).all()
        serializer = ListAllSerializer(obj, many=True)
        return Response(serializer.data, status=200)

class CostCalculator(views.APIView):
    def get(self, request):
        size = request.GET.get('size')
        length = request.GET.get('length')
        cost = 5
        if int(size) > 500*1024*1024:
            cost = 12.5

        if int(length) > 6*60+18:
            cost += 20
        else:
            cost+=12.5

        return Response({
            'cost':cost,
        }, status=200)