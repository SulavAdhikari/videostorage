from rest_framework import serializers
from moviepy.editor import VideoFileClip

from videostorage.settings import UPLOAD_LIMIT
from .models import Video

class Videoserializer(serializers.ModelSerializer):\

    title = serializers.CharField(read_only=True)
    cost = serializers.IntegerField(read_only=True)
    size = serializers.IntegerField(read_only=True)

    class Meta:
        model = Video
        fields = "__all__"

    def calculate_cost(self, video, clip):
        cost=0
        if video.size < 500*1024*1024:
            cost += 5
        else:
            cost+=12.5
        if clip.duration > (6*60)+18:
            cost+=20
        return cost

    def validate(self, data):
        video = data.get('video')
        if video.name.endswith('.mp4') or video.name.endswith('.mkv'):
            
            clip =  VideoFileClip(video.temporary_file_path())
            duration = clip.duration
            
            if duration > 10*60:
                raise serializers.ValidationError({
                'message':'video exceeds length limit'
                })
            print(video.size)
            if video.size > UPLOAD_LIMIT:
                raise serializers.ValidationError({
                'message':'file is too big'
            })

            cost = self.calculate_cost(video, clip)        
            
            obj = Video(title=video.name,video=video, size=video.size, cost=cost)
            return{
                'title':video.name,
                'video':video,
                'size':video.size,
                'cost':cost,
            }
        else:
            raise serializers.ValidationError({
                'message':'invalid file type'
            },)
