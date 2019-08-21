FROM sparkfish.azurecr.io/alpine-flask-cairo:latest

WORKDIR /code

COPY requirements.txt /code
#ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk add openssl
RUN /env/bin/pip install -r /code/requirements.txt

COPY . /code/

ENV FLASK_APP main.py
ENV FLASK_ENV production
ENV FLASK_RUN_HOST 0.0.0.0
WORKDIR /code/

EXPOSE 8000 8000
CMD /env/bin/gunicorn --bind 0.0.0.0:8000 main:app --workers 2 --threads 12 --reload