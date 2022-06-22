FROM python:3.9.6

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install gcc libpq-dev python3-dev netcat git

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /opt/app/deploy/python/django/run.sh

ENTRYPOINT ["/opt/app/deploy/python/django/run.sh"]
