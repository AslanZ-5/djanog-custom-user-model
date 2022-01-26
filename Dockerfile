FROM python:3

# create and set working directory

WORKDIR /app

# Add current directory code to working directory 
ADD . /app/

# set default environment variables 
ENV PYTHONBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND = noninteractive 
# set project environment variable 
# grab these via Python's os.environ
# these are 100% option here 


# Install system dependencies 
RUN pip install -r requirements.txt
CMD ["python3","manage.py","runserver","0.0.0.0:8888"]