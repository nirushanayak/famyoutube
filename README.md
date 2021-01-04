# famyoutube
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time 
from YouTube for a given tag/search query in a paginated response.

1.docker image for this project is available in :
  https://hub.docker.com/r/nirushadoc/famyoutube/tags?page=1&ordering=last_updated

2.to pull the image :
  docker pull nirushadoc/famyoutube:final

3.to run the project locally :
  1. git clone the repository 
      git clone 
  1. pip install -r requirement.txt
  2. run ./run.sh script
      this will run python manage.py runserver at port 8000 and also will start a q_cluster process wich is scheduled every 2 mins to pull latest youtube videos


   
