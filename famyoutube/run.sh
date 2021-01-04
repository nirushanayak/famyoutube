#!/bin/bash

python manage.py runserver &
P1=$!
python manage.py qcluster &
P2=$!
wait $P1 $P2
