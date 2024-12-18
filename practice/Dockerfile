FROM python:3.12

RUN mkdir /app
COPY . /app
WORKDIR /app
COPY /requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD cd /practice && python3 -m manage runserver




