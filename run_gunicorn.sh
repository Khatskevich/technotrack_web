#!/bin/bash  
gunicorn --reload -b localhost:8000 technotrack_web.wsgi:application

