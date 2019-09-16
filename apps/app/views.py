from rest_framework.viewsets import ModelViewSet
from .serializers import VideoSerializer, SongSerializer
# Create your views here.


class VideoViewSet(ModelViewSet):
    queryset = VideoSerializer.Meta.model.objects.all()
    serializer_class = VideoSerializer


class SongViewSet(ModelViewSet):
    queryset = SongSerializer.Meta.model.objects.all()
    serializer_class = SongSerializer


