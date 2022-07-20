from rest_framework import serializers
from moviepy.editor import VideoFileClip

from videostorage.settings import UPLOAD_LIMIT
from .models import Video

class Videoserializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    length = serializers.IntegerField(read_only=True)
    size = serializers.IntegerField(read_only=True)

    class Meta:
        model = Video
        fields = "__all__"

    def validate(self, data):
        video = data.get('video')
        if video.name.endswith('.mp4') or video.name.endswith('.mkv'):
            
            clip =  VideoFileClip(video.temporary_file_path())
            duration = clip.duration
            
            if duration > 10*60:
                raise serializers.ValidationError({
                'message':'video exceeds length limit'
                })
           
            if video.size > UPLOAD_LIMIT:
                raise serializers.ValidationError({
                'message':'file is too big'
            })
   
            return{
                'title':video.name,
                'video':video,
                'size':video.size,
                'length':duration
            }
        else:
            raise serializers.ValidationError({
                'message':'invalid file type'
            },)


class ListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'




