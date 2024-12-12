FROM python:3.12

RUN mkdir /app
COPY . /app
WORKDIR /app
COPY /requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000
RUN python3 -m manage runserver 0.0.0.0:8000




