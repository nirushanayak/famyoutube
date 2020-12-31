import requests
from django.conf import  settings
from .models import Videos

def get_youtube_video_data():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'q': 'cricket',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 10,
        'type': 'video'
    }

    r = requests.get(search_url, params=search_params)
    print(r.text)
    items = r.json()["items"]
    print(r)
    for item in items:
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        datetime = item["snippet"]["publishTime"]
        Videos.objects.update_or_create(
            title=title, description=description, datatime1=datetime)
