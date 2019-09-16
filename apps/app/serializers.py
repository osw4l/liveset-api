from rest_framework import serializers
from .models import Video, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id',
            'name',
            'file',
            'active'
        )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id',
            'name',
            'file',
            'active'
        )


