FROM alpine:3

RUN apk add --update \
    openssh \
    cairo libffi-dev libc6-compat \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
    libreoffice \
    git \
    npm nodejs \
    musl-dev linux-headers \
    libxslt-dev \
    zlib-dev jpeg-dev \
    && rm -rf /var/cache/apk/*

RUN python3 -m ensurepip
RUN git clone https://github.com/unoconv/unoconv

WORKDIR /code

COPY requirements.txt /code
ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk add openssl
 
RUN pip install wheel
RUN pip install -r /code/requirements.txt

COPY . /code/

ENV UNOCONV_PATH unoconv/unoconv
ENV FLASK_APP main.py
ENV FLASK_ENV production
ENV FLASK_RUN_HOST 0.0.0.0
ENV MAX_CONTENT_LENGTH 31457280
ENV UPLOAD_RATE_LIMIT 15 per minute
WORKDIR /code/

EXPOSE 5000 5000
CMD gunicorn --bind 0.0.0.0:5000 main:app --workers 2 --threads 12 --reload
