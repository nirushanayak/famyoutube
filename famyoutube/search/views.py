from .models import Videos
from .serializers import VideosSerializers
from rest_framework import generics
from rest_framework import filters
import requests
from django.conf import settings

class VideosList(generics.ListCreateAPIView):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'q': 'cricket',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 10,
        'type': 'video'
    }

    r = requests.get(search_url, params=search_params)
    print("views")
    print(r)

    queryset = Videos.objects.all().order_by('-datetime1')
    serializer_class = VideosSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
