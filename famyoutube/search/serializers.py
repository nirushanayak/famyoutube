from .models import Videos

from rest_framework import serializers


class VideosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videos
        fields = ['title', 'description', 'datetime1']
