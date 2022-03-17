FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000

#COPY --from=node /app/src/main/static /app/src/main/static
#
#RUN python3 src/manage.py collectstatic --noinput
#
#CMD python3 src/manage.py migrate && gunicorn webmonitoring.wsgi --chdir src --bind 0.0.0.0 --preload --log-file -
