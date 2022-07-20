from rest_framework.generics import ListAPIView
from rest_framework import views
from rest_framework.response import Response 

from videostorage.settings import UPLOAD_LIMIT
from .serializers import Videoserializer, ListAllSerializer
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
    
class AllVideosListView(ListAPIView):
    model = Video
    serializer_class = ListAllSerializer
    queryset = Video.objects.all()

class FilterVideos(views.APIView):

    serializer_class = ListAllSerializer

    def get(self, request):
        data = request.GET
        title = data.get('title')
        obj = Video.objects.filter(title__contains=title).all()
        serializer = ListAllSerializer(obj, many=True)
        return Response(serializer.data, status=200)