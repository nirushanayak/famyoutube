import requests
from django.conf import  settings
from .models import Videos
from dateutil import relativedelta

def get_youtube_video_data():
    print("task started")
    from datetime import datetime
    now = datetime.now()
    time = now - relativedelta.relativedelta(months=1)
    time = time.isoformat("T") + "Z"
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'q': 'cricket',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'type': 'video',
        'maxRecord': 49,
        'publishedAfter': time,
        'pageToken':'',
    }
    array_no=0
    while(True):
        r = requests.get(search_url, params=search_params)
        page_token = r.json().get("nextPageToken")
        search_params['pageToken'] = page_token
        if r.status_code == 200:
            items = r.json()["items"]
            for item in items:
                title = item["snippet"]["title"]
                description = item["snippet"]["description"]
                datetime = item["snippet"]["publishTime"]
                Videos.objects.update_or_create(
                    title=title, description=description, datetime1=datetime)
            if not page_token:
                break
        elif r.status_code == 403 : #suport for multiple api keys , if limit exceeds quota
            print("quota exceeded, availing different api key")
            settings.YOUTUBE_DATA_API_KEY = settings.API_KEYS[array_no]
            array_no +=1
            if array_no > len(settings.API_KEYS)-1:
                break
        else:
            print("falied with status code : ",r.status_code)
            break
    print("task completed")
