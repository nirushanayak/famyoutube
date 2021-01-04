from .models import Videos
from .serializers import VideosSerializers
from rest_framework import generics
from rest_framework import filters

class VideosList(generics.ListCreateAPIView):
    queryset = Videos.objects.all().order_by('-datetime1')
    serializer_class = VideosSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
